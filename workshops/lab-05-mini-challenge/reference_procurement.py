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
    - request_status: "Ready" or "Incomplete"
    - missing_fields: รายการข้อมูลที่ขาดหายไป (list, ว่างได้ถ้าครบ)
    - budget_concern: ข้อสังเกตเรื่องงบประมาณ (string, ระบุ "None" ถ้าไม่มี)
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
