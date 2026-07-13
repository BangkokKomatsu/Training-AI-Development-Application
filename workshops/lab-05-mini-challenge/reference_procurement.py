# ตัวอย่างอ้างอิง (Reference Example) - งานจัดซื้อ
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

def analyze_purchase_request(user_input):
    prompt = f"""
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
    - request_status: "Ready" or "Incomplete"
    - missing_fields: รายการข้อมูลที่ขาดหายไป (list, ว่างได้ถ้าครบ)
    - budget_concern: ข้อสังเกตเรื่องงบประมาณ (string, ระบุ "None" ถ้าไม่มี)
    - recommended_next_step: ขั้นตอนถัดไปที่ควรทำ

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

st.set_page_config(page_title="Purchase Request Analyzer", page_icon="🛒", layout="centered")
st.title("🛒 Purchase Request Analyzer")
st.caption("ตัวอย่างอ้างอิง: AI ช่วยตรวจสอบคำขอซื้อว่าข้อมูลครบก่อนส่งอนุมัติหรือไม่")
st.divider()

with st.container(border=True):
    input_text = st.text_area(
        "วางข้อความคำขอซื้อที่ต้องการให้ AI ตรวจสอบ:",
        height=120,
        placeholder="เช่น: ขอซื้อสายพาน (Belt) สำรองสำหรับไลน์ผลิตที่ 3 ด่วนมาก เพราะของเดิมขาดและเครื่องหยุดผลิตอยู่ ยังไม่มีใบเสนอราคาจาก Supplier และยังไม่ได้ระบุจำนวนที่ต้องการ",
    )
    run_clicked = st.button("🚀 ตรวจสอบคำขอซื้อ", type="primary", use_container_width=True)

if run_clicked:
    if not input_text.strip():
        st.warning("กรุณากรอกข้อมูลก่อน")
    else:
        with st.spinner("AI กำลังตรวจสอบ..."):
            try:
                result = analyze_purchase_request(input_text)

                st.divider()
                status = result.get("request_status", "")
                if status == "Ready":
                    st.success(f"✅ สถานะ: {status}")
                else:
                    st.warning(f"⚠️ สถานะ: {status}")

                missing = result.get("missing_fields") or []
                if missing:
                    st.markdown("**ข้อมูลที่ขาดหายไป:**")
                    for m in missing:
                        st.markdown(f"- {m}")

                st.markdown(f"**ข้อสังเกตเรื่องงบประมาณ:** {result.get('budget_concern')}")
                st.markdown(f"**ขั้นตอนถัดไป:** {result.get('recommended_next_step')}")

                with st.expander("ดูข้อมูล JSON ต้นฉบับ"):
                    st.json(result)

            except Exception as e:
                st.error(f"เกิดข้อผิดพลาด: {e}")
