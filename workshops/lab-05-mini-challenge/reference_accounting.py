# ตัวอย่างอ้างอิง (Reference Example) - งานบัญชี
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

def analyze_invoice(user_input):
    prompt = f"""
    คุณเป็นผู้ช่วย AI สำหรับฝ่ายบัญชี (Accounting)

    Task:
    ตรวจสอบใบแจ้งหนี้หรือใบขอเบิกแบบไม่เป็นทางการ (ที่พนักงานสรุปมาให้) ว่าพร้อมตั้งเบิกจ่ายหรือไม่

    Context:
    พนักงานมักส่งรายละเอียดใบแจ้งหนี้หรือใบขอเบิกเป็นข้อความสรุป (แชท/อีเมล) แทนการกรอกผ่านระบบบัญชี
    โดยตรง ฝ่ายบัญชีต้องเช็คว่ายอดเงินตรงกับ PO และเอกสารประกอบครบก่อนดำเนินการตั้งเบิก

    Rules:
    - ห้ามเดาข้อมูลใดๆ ที่ไม่ได้ระบุไว้ในข้อมูลนำเข้า
    - ถ้ามีการระบุยอดใน PO และยอดในใบแจ้งหนี้ไม่ตรงกัน ให้ระบุส่วนต่างไว้ใน field "amount_mismatch"
      (ระบุ "None" ถ้าไม่มีการระบุ PO หรือยอดตรงกัน)
    - ระบุเอกสารประกอบที่ควรมีแต่ไม่ได้กล่าวถึงในข้อมูลนำเข้า
      (เช่น ใบกำกับภาษี, ใบส่งของ, ใบเสร็จรับเงิน)
    - แนะนำขั้นตอนถัดไปก่อนตั้งเบิกจ่าย

    Output format:
    ตอบกลับเป็น JSON เท่านั้น โดยมี field ดังนี้:
    - invoice_status: "Ready to Process" or "Needs Review"
    - amount_mismatch: ข้อความอธิบายส่วนต่างยอดเงิน (string, ระบุ "None" ถ้าไม่มี)
    - missing_documents: รายการเอกสารประกอบที่ขาดหายไป (list, ว่างได้ถ้าครบ)
    - recommended_next_step: ขั้นตอนถัดไปที่ควรทำ

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

st.set_page_config(page_title="Invoice Verification Assistant", page_icon="🧾", layout="centered")
st.title("🧾 Invoice Verification Assistant")
st.caption("ตัวอย่างอ้างอิง: AI ช่วยตรวจสอบใบแจ้งหนี้/ใบขอเบิกว่าพร้อมตั้งเบิกจ่ายหรือไม่")
st.divider()

with st.container(border=True):
    input_text = st.text_area(
        "วางข้อความใบแจ้งหนี้หรือใบขอเบิกที่ต้องการให้ AI ตรวจสอบ:",
        height=120,
        placeholder="เช่น: ใบแจ้งหนี้จาก Supplier ค่าซ่อมเครื่องจักร 45000 บาท อ้างอิง PO-2026-088 แต่ยอดใน PO ระบุไว้ 42000 บาท ยังไม่แนบใบกำกับภาษี",
    )
    run_clicked = st.button("🚀 ตรวจสอบใบแจ้งหนี้", type="primary", use_container_width=True)

if run_clicked:
    if not input_text.strip():
        st.warning("กรุณากรอกข้อมูลก่อน")
    else:
        with st.spinner("AI กำลังตรวจสอบ..."):
            try:
                result = analyze_invoice(input_text)

                st.divider()
                status = result.get("invoice_status", "")
                if status == "Ready to Process":
                    st.success(f"✅ สถานะ: {status}")
                else:
                    st.warning(f"⚠️ สถานะ: {status}")

                mismatch = result.get("amount_mismatch")
                if mismatch and mismatch != "None":
                    st.error(f"💰 ยอดเงินไม่ตรงกัน: {mismatch}")

                missing = result.get("missing_documents") or []
                if missing:
                    st.markdown("**เอกสารประกอบที่ขาดหายไป:**")
                    for m in missing:
                        st.markdown(f"- {m}")

                st.markdown(f"**ขั้นตอนถัดไป:** {result.get('recommended_next_step')}")

                with st.expander("ดูข้อมูล JSON ต้นฉบับ"):
                    st.json(result)

            except Exception as e:
                st.error(f"เกิดข้อผิดพลาด: {e}")
