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
PROMPT_BUILDERS = {
    "Factory Issue": lambda text: f"""
    You are an AI assistant for factory issue management.
    Analyze the factory issue report.

    Rules:
    - Do not assume or invent any information that is not in the input.
    - Choose category only from: Mechanical, Electrical, QA/QC, Safety, Other.
    - Set priority as Low, Medium, or High. If the input does not give enough detail to
      determine priority, use "Unknown" instead of guessing.
    - List anything needed to classify this issue confidently but missing from the input
      in the "missing_information" field (empty list if nothing is missing).
    - Add a "confidence" field: High, Medium, or Low, based on how complete the input is.

    Return JSON only with these fields:
    category, priority, summary, missing_information, confidence

    Issue report:
    {text}
    """,
    "Purchasing": lambda text: f"""
    You are an AI assistant for the Purchasing department.

    Task:
    Review an informal purchase request (written by an employee) and check if it's
    ready to submit for approval.

    Context:
    Employees submit purchase requests as free-text messages (chat/email), not through
    a structured form. The requests are often written in a hurry and may be missing
    fields that Purchasing needs before processing.

    Rules:
    - Do not assume any information that is not stated in the input.
    - Identify required fields for a purchase request that are missing
      (e.g. quantity, budget code, vendor, needed-by date).
    - Flag a budget concern if the request mentions a high cost or urgent/rush order
      without justification.
    - Suggest the next step to move this request forward.

    Output format:
    Return JSON only with these fields:
    request_status, missing_fields, budget_concern, recommended_next_step

    Input text:
    {text}
    """,
    "Production Planning": lambda text: f"""
    You are an AI assistant for the Production Planning department.

    Task:
    Read an informal daily production note (written by a line supervisor) and
    summarize it for the planning team.

    Context:
    Line supervisors write short, informal status updates at the end of each shift
    (e.g. a chat message or handwritten log) instead of filling a formal report. The
    planning team needs a quick, structured summary to spot risks to tomorrow's schedule.

    Rules:
    - Do not assume any information that is not stated in the input.
    - Identify any bottleneck or risk that could delay the production plan.
    - List resources needed to resolve the issue, if any
      (e.g. manpower, spare parts, raw material).
    - Suggest a recommended action for the planning team.

    Output format:
    Return JSON only with these fields:
    plan_summary, bottleneck_risk, resource_needed, recommended_action

    Input text:
    {text}
    """,
    "Safety Checklist": lambda text: f"""
    You are an AI assistant for the Safety department.

    Task:
    Review an informal work description (written by a worker or supervisor before
    starting a task) and check whether it shows the basic safety precautions in place.

    Context:
    Workers often describe an upcoming task informally (relayed to a supervisor, or a
    short note) before starting, without going through a formal safety checklist form.
    This is a pre-work check — the task has not started yet, so this is not an incident
    report.

    Rules:
    - Do not assume any precaution that is not stated in the input.
    - Identify safety precautions or PPE (Personal Protective Equipment) that should normally
      apply to this type of work but are not mentioned in the input.
    - Do not classify or rate the severity of any incident — this text describes work about to
      start, not an incident that already happened.
    - Suggest what should be confirmed or prepared before the work begins.

    Output format:
    Return JSON only with these fields:
    readiness_status, missing_precautions, recommended_action

    Input text:
    {text}
    """,
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
            {"role": "system", "content": "You are a helpful AI assistant. Return JSON only."},
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
