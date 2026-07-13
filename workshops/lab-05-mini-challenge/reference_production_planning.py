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
    - plan_summary: สรุปสถานการณ์การผลิตแบบสั้น กระชับ
    - bottleneck_risk: ความเสี่ยงที่อาจทำให้แผนล่าช้า (ระบุ "None" ถ้าไม่มี)
    - resource_needed: ทรัพยากรที่ต้องการเพิ่มเติม (list, ว่างได้ถ้าไม่ต้องการ)
    - recommended_action: ข้อเสนอแนะสำหรับทีมวางแผน

    Input text:
    {user_input}
    """
    response = client.chat.completions.create(
        model=deployment_name,
        messages=[
            {"role": "system", "content": "You are a helpful AI assistant. Return JSON only."},
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
