import json
import os
import time
import pandas as pd
import streamlit as st
from dotenv import load_dotenv
from openai import AzureOpenAI
import io

# 1. โหลด Environment Variables
load_dotenv()
client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
)
deployment_name = os.getenv("AZURE_OPENAI_DEPLOYMENT")

# 2. Prompt ของแต่ละแผนก/หัวข้อ (เลือกได้จาก dropdown ด้านล่าง)
# ทุกไฟล์ sample-data ที่ใช้กับหน้านี้ต้องมีคอลัมน์ชื่อ "issue_report" เป็นข้อความที่จะให้ AI วิเคราะห์
def build_factory_issue_prompt(text):
    return f"""
    คุณเป็นผู้ช่วย AI สำหรับจัดการปัญหาในโรงงาน
    วิเคราะห์รายงานปัญหาโรงงาน

    Rules:
    - ห้ามเดาหรือแต่งข้อมูลใดๆ ที่ไม่มีอยู่ในข้อมูลนำเข้า
    - เลือกหมวดหมู่ (category) จากรายการนี้เท่านั้น: Mechanical, Electrical, QA/QC, Safety, Other
    - กำหนดความเร่งด่วน (priority) เป็น Low, Medium หรือ High ถ้าข้อมูลนำเข้าไม่มีรายละเอียดพอ
      ที่จะกำหนดความเร่งด่วน ให้ใช้ "Unknown" แทนการเดา
    - ระบุสิ่งที่จำเป็นต่อการจัดหมวดหมู่ปัญหานี้อย่างมั่นใจแต่ขาดหายไปจากข้อมูลนำเข้า
      ไว้ใน field "missing_information" (list ว่างได้ถ้าไม่มีอะไรขาด)
    - เพิ่ม field "confidence": High, Medium หรือ Low ตามความครบถ้วนของข้อมูลนำเข้า

    ตอบกลับเป็น JSON เท่านั้น โดยมี field ดังนี้:
    category, priority, summary, missing_information, confidence

    รายงานปัญหา:
    {text}
    """

def build_purchasing_prompt(text):
    return f"""
    คุณเป็นผู้ช่วย AI สำหรับฝ่ายจัดซื้อ (Purchasing)

    Task:
    ตรวจสอบคำขอซื้อแบบไม่เป็นทางการ (ที่พนักงานเขียน) ว่าพร้อมส่งขออนุมัติหรือไม่

    Context:
    พนักงานส่งคำขอซื้อเป็นข้อความอิสระ (แชท/อีเมล) ไม่ได้กรอกผ่านฟอร์มที่มีโครงสร้าง
    คำขอมักเขียนขึ้นอย่างรีบเร่งและอาจขาดข้อมูลที่ฝ่ายจัดซื้อต้องใช้ก่อนดำเนินการ

    Rules:
    - ห้ามเดาข้อมูลใดๆ ที่ไม่ได้ระบุไว้ในข้อมูลนำเข้า
    - ระบุ field ที่จำเป็นสำหรับคำขอซื้อที่ขาดหายไป
      (เช่น จำนวน, budget code, vendor, วันที่ต้องการ)
    - แจ้งเตือนข้อสังเกตเรื่องงบประมาณ ถ้าคำขอกล่าวถึงค่าใช้จ่ายสูงหรือคำสั่งเร่งด่วน
      โดยไม่มีเหตุผลประกอบ
    - แนะนำขั้นตอนถัดไปเพื่อผลักดันคำขอนี้ต่อ

    Output format:
    ตอบกลับเป็น JSON เท่านั้น โดยมี field ดังนี้:
    request_status, missing_fields, budget_concern, recommended_next_step

    ข้อความนำเข้า:
    {text}
    """

def build_production_planning_prompt(text):
    return f"""
    คุณเป็นผู้ช่วย AI สำหรับฝ่ายวางแผนการผลิต (Production Planning)

    Task:
    อ่านบันทึกการผลิตประจำวันแบบไม่เป็นทางการ (ที่หัวหน้าไลน์เขียน) แล้วสรุปให้ทีมวางแผน

    Context:
    หัวหน้าไลน์มักเขียนสรุปสถานะสั้นๆ แบบไม่เป็นทางการตอนท้ายกะ
    (เช่น ข้อความแชทหรือบันทึกลายมือ) แทนการกรอกรายงานที่เป็นทางการ ทีมวางแผน
    ต้องการสรุปแบบมีโครงสร้างอย่างรวดเร็วเพื่อระบุความเสี่ยงต่อแผนงานวันถัดไป

    Rules:
    - ห้ามเดาข้อมูลใดๆ ที่ไม่ได้ระบุไว้ในข้อมูลนำเข้า
    - ระบุคอขวด (bottleneck) หรือความเสี่ยงที่อาจทำให้แผนการผลิตล่าช้า
    - ระบุทรัพยากรที่ต้องใช้แก้ปัญหา ถ้ามี
      (เช่น กำลังคน, อะไหล่, วัตถุดิบ)
    - แนะนำการดำเนินการสำหรับทีมวางแผน

    Output format:
    ตอบกลับเป็น JSON เท่านั้น โดยมี field ดังนี้:
    plan_summary, bottleneck_risk, resource_needed, recommended_action

    ข้อความนำเข้า:
    {text}
    """

def build_safety_checklist_prompt(text):
    return f"""
    คุณเป็นผู้ช่วย AI สำหรับฝ่ายความปลอดภัย (Safety)

    Task:
    ตรวจสอบคำอธิบายงานแบบไม่เป็นทางการ (ที่คนงานหรือหัวหน้างานเขียนไว้ก่อนเริ่มงาน)
    ว่ามีมาตรการความปลอดภัยพื้นฐานครบถ้วนหรือไม่

    Context:
    คนงานมักอธิบายงานที่กำลังจะเริ่มแบบไม่เป็นทางการ (บอกต่อหัวหน้างาน หรือเขียนโน้ตสั้นๆ)
    ก่อนเริ่มงาน โดยไม่ได้กรอกแบบฟอร์มตรวจสอบความปลอดภัยที่เป็นทางการ นี่คือการตรวจสอบ
    ก่อนเริ่มงาน (pre-work check) — งานยังไม่ได้เริ่ม จึงไม่ใช่รายงานอุบัติเหตุ

    Rules:
    - ห้ามเดามาตรการป้องกันใดๆ ที่ไม่ได้ระบุไว้ในข้อมูลนำเข้า
    - ระบุมาตรการความปลอดภัยหรือ PPE (อุปกรณ์ป้องกันส่วนบุคคล) ที่ปกติควรมีสำหรับงานประเภทนี้
      แต่ไม่ได้ถูกกล่าวถึงในข้อมูลนำเข้า
    - ห้ามจัดหมวดหมู่หรือประเมินความรุนแรงของอุบัติเหตุ — ข้อความนี้อธิบายงานที่กำลังจะเริ่ม
      ไม่ใช่อุบัติเหตุที่เกิดขึ้นแล้ว
    - แนะนำสิ่งที่ควรยืนยันหรือเตรียมก่อนเริ่มงาน

    Output format:
    ตอบกลับเป็น JSON เท่านั้น โดยมี field ดังนี้:
    readiness_status, missing_precautions, recommended_action

    ข้อความนำเข้า:
    {text}
    """

PROMPT_BUILDERS = {
    "Factory Issue": build_factory_issue_prompt,
    "Purchasing": build_purchasing_prompt,
    "Production Planning": build_production_planning_prompt,
    "Safety Checklist": build_safety_checklist_prompt,
}

SAMPLE_FILE_HINT = {
    "Factory Issue": "sample-data/factory_issues_sample.xlsx",
    "Purchasing": "sample-data/purchase_requests_sample.csv",
    "Production Planning": "sample-data/production_notes_sample.csv",
    "Safety Checklist": "sample-data/safety_checklist_notes_sample.csv",
}

# 3. ฟังก์ชันวิเคราะห์ปัญหา
def analyze_issue(issue_report, department):
    prompt = PROMPT_BUILDERS[department](issue_report)
    response = client.chat.completions.create(
        model=deployment_name,
        messages=[
            {"role": "system", "content": "คุณเป็นผู้ช่วย AI ที่คอยช่วยเหลือผู้ใช้งาน ตอบกลับเป็น JSON เท่านั้น"},
            {"role": "user", "content": prompt},
        ],
        response_format={ "type": "json_object" }
    )
    return json.loads(response.choices[0].message.content)

# TODO: เขียนฟังก์ชัน get_action_required(priority) เหมือนที่ทำใน starter.py / solution.py
# (ใช้ได้เฉพาะตอนเลือกแผนก "Factory Issue" เพราะมี field "priority" เท่านั้น แผนกอื่นไม่มี field นี้)
# ใบ้: ใช้ if/elif/else เช็คค่า priority ("High"/"Medium"/อื่นๆ) แล้ว return ข้อความสิ่งที่ต้องทำต่อ
# def get_action_required(priority):
#     if priority == "High":
#         return "..."
#     elif priority == "Medium":
#         return "..."
#     return "..."

# 4. หน้าเว็บ Streamlit
st.set_page_config(page_title="Factory Batch Processor", page_icon="📑")
st.title("📑 AI Excel Batch Processor")
st.markdown("ระบบอัปโหลดไฟล์ Excel/CSV ให้ AI ช่วยวิเคราะห์ทีละแถว เลือกแผนก/หัวข้อข้อมูลด้านล่างให้ตรงกับไฟล์ที่อัปโหลด")

department = st.selectbox("เลือกแผนก/หัวข้อข้อมูล", list(PROMPT_BUILDERS.keys()))
st.caption(f"ไฟล์ตัวอย่างสำหรับหัวข้อนี้: `{SAMPLE_FILE_HINT[department]}`")

uploaded_file = st.file_uploader("อัปโหลดไฟล์รายงาน (Excel / CSV)", type=['xlsx', 'csv'])

if uploaded_file is not None:
    # อ่านไฟล์ที่อัปโหลด
    if uploaded_file.name.endswith('.csv'):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    st.write("ข้อมูลก่อนประมวลผล:")
    st.dataframe(df.head())

    if st.button("🚀 เริ่มการวิเคราะห์ข้อมูลด้วย AI", type="primary"):
        # เตรียม Progress Bar
        progress_bar = st.progress(0)
        status_text = st.empty()

        results = []
        total_rows = len(df)

        # วนลูปวิเคราะห์ทีละบรรทัด
        for index, row in df.iterrows():
            status_text.text(f"กำลังประมวลผลบรรทัดที่ {index + 1} จาก {total_rows}...")

            # สมมุติว่าในไฟล์มีคอลัมน์ชื่อ 'issue_report'
            report_text = row.get('issue_report', str(row.values))

            try:
                ai_result = analyze_issue(report_text, department)
                if department == "Factory Issue":
                    missing_info = ai_result.get("missing_information") or []
                    results.append({
                        "AI_Category": ai_result.get("category"),
                        "AI_Priority": ai_result.get("priority"),
                        "AI_Summary": ai_result.get("summary"),
                        "AI_Missing_Info": ", ".join(missing_info) if isinstance(missing_info, list) else missing_info,
                        "AI_Confidence": ai_result.get("confidence"),
                        # TODO: เพิ่ม "AI_Action_Required": get_action_required(ai_result.get("priority")) ตรงนี้
                    })
                else:
                    # แผนกอื่นๆ: field ของแต่ละแผนกไม่เหมือนกัน จึงสร้างคอลัมน์ตาม field ที่ AI ส่งกลับมาโดยตรง
                    results.append({
                        f"AI_{key}": (", ".join(value) if isinstance(value, list) else value)
                        for key, value in ai_result.items()
                    })
            except Exception as e:
                results.append({"AI_Error": str(e)})

            time.sleep(1)  # กันชน Rate Limit เวลาหลายคนรันพร้อมกัน

            # อัปเดต Progress Bar
            progress_bar.progress((index + 1) / total_rows)

        status_text.text("ประมวลผลเสร็จสมบูรณ์! 🎉")

        # นำผลลัพธ์มารวมกับ DataFrame เดิม
        result_df = pd.DataFrame(results)
        final_df = pd.concat([df, result_df], axis=1)

        st.write("ข้อมูลหลังประมวลผล:")
        st.dataframe(final_df)

        # สร้างไฟล์ Excel บนหน่วยความจำสำหรับให้ดาวน์โหลด
        buffer = io.BytesIO()
        with pd.ExcelWriter(buffer, engine='openpyxl') as writer:
            final_df.to_excel(writer, index=False)

        st.download_button(
            label="📥 ดาวน์โหลดไฟล์ Excel ผลลัพธ์",
            data=buffer.getvalue(),
            file_name="factory_issues_analyzed.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
