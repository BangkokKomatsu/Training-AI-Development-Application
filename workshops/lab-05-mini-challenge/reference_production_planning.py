# ตัวอย่างอ้างอิง (Reference Example) - งานวางแผนการผลิต
# เปิดไฟล์นี้ดูเป็นแนวทางก่อนเริ่มออกแบบ Use Case ของตัวเองใน app_streamlit_template.py
# ไม่ใช่หนึ่งใน 5 หัวข้อที่ต้องเลือกใน README (ดู README.md)

import json
import os
import streamlit as st
from dotenv import load_dotenv
from openai import AzureOpenAI

load_dotenv()
client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
)
deployment_name = os.getenv("AZURE_OPENAI_DEPLOYMENT")

def analyze_production_note(user_input):
    prompt = f"""
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
    - plan_summary: สรุปสถานการณ์การผลิตแบบสั้น กระชับ
    - bottleneck_risk: ความเสี่ยงที่อาจทำให้แผนล่าช้า (ระบุ "None" ถ้าไม่มี)
    - resource_needed: ทรัพยากรที่ต้องการเพิ่มเติม (list, ว่างได้ถ้าไม่ต้องการ)
    - recommended_action: ข้อเสนอแนะสำหรับทีมวางแผน

    ข้อความนำเข้า:
    {user_input}
    """
    response = client.chat.completions.create(
        model=deployment_name,
        messages=[
            {"role": "system", "content": "คุณเป็นผู้ช่วย AI ที่คอยช่วยเหลือผู้ใช้งาน ตอบกลับเป็น JSON เท่านั้น"},
            {"role": "user", "content": prompt},
        ],
        response_format={ "type": "json_object" }
    )
    return json.loads(response.choices[0].message.content)

st.set_page_config(page_title="Production Plan Summarizer", page_icon="🏭", layout="centered")
st.title("🏭 Production Plan Summarizer")
st.caption("ตัวอย่างอ้างอิง: AI ช่วยสรุปบันทึกหน้างานประจำวันให้ทีมวางแผนการผลิต")
st.divider()

with st.container(border=True):
    input_text = st.text_area(
        "วางบันทึกหน้างานที่ต้องการให้ AI สรุป:",
        height=120,
        placeholder="เช่น: ไลน์ผลิต 2 กะดึกวันนี้ผลิตได้ช้ากว่าแผน 15% เนื่องจากขาดพนักงานประกอบชิ้นงาน 2 คน (ลาป่วยกะทันหัน) คาดว่าจะกระทบยอดส่งมอบของลูกค้าพรุ่งนี้เช้า",
    )
    run_clicked = st.button("🚀 สรุปด้วย AI", type="primary", use_container_width=True)

if run_clicked:
    if not input_text.strip():
        st.warning("กรุณากรอกข้อมูลก่อน")
    else:
        with st.spinner("AI กำลังสรุป..."):
            try:
                result = analyze_production_note(input_text)

                st.divider()
                st.markdown(f"**สรุปสถานการณ์:** {result.get('plan_summary')}")

                risk = result.get("bottleneck_risk")
                if risk and risk != "None":
                    st.warning(f"⚠️ ความเสี่ยง: {risk}")
                else:
                    st.success("✅ ไม่มีความเสี่ยงที่ระบุ")

                resources = result.get("resource_needed") or []
                if resources:
                    st.markdown("**ทรัพยากรที่ต้องการเพิ่มเติม:**")
                    for r in resources:
                        st.markdown(f"- {r}")

                st.markdown(f"**ข้อเสนอแนะ:** {result.get('recommended_action')}")

                with st.expander("ดูข้อมูล JSON ต้นฉบับ"):
                    st.json(result)

            except Exception as e:
                st.error(f"เกิดข้อผิดพลาด: {e}")
