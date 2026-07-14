# ตัวอย่างอ้างอิง (Reference Example) - งาน Safety
# เปิดไฟล์นี้ดูเป็นแนวทางก่อนเริ่มออกแบบ Use Case ของตัวเองใน app_streamlit_template.py
#
# หมายเหตุ: ตัวอย่างนี้เน้น "ตรวจสอบความพร้อมก่อนเริ่มงาน" (pre-work safety checklist)
# ซึ่งเป็นคนละมุมกับตัวเลือกข้อ 2 ในลิสต์ Mini Challenge ("Safety Incident Classifier" ที่จัดหมวดหมู่
# อุบัติเหตุที่เกิดขึ้นแล้ว) ดังนั้นยังเลือกทำหัวข้อ Safety Incident Classifier เป็น mini challenge ของ
# ตัวเองได้ตามปกติ ไม่ซ้ำกับตัวอย่างนี้

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

def analyze_safety_checklist(user_input):
    prompt = f"""
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
    - readiness_status: "Ready" or "Not Ready" or "Cannot Determine"
    - missing_precautions: รายการข้อควรระวัง/PPE ที่ควรมีแต่ไม่ได้ระบุไว้ (list, ว่างได้ถ้าครบ)
    - recommended_action: สิ่งที่ควรยืนยัน/เตรียมก่อนเริ่มงาน

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

st.set_page_config(page_title="Safety Checklist Reviewer", page_icon="🦺", layout="centered")
st.title("🦺 Safety Checklist Reviewer")
st.caption("ตัวอย่างอ้างอิง: AI ช่วยตรวจสอบความพร้อมด้านความปลอดภัยก่อนเริ่มงาน")
st.divider()

with st.container(border=True):
    input_text = st.text_area(
        "วางข้อความอธิบายงานที่กำลังจะเริ่ม เพื่อให้ AI ตรวจสอบความพร้อม:",
        height=120,
        placeholder="เช่น: จะขึ้นไปซ่อมไฟส่องสว่างที่ความสูง 3 เมตรบริเวณไลน์ผลิต 1 โดยใช้บันไดพาดกับผนัง ยังไม่ได้ขอใบอนุญาตทำงานที่สูง (Work at Height Permit)",
    )
    run_clicked = st.button("🚀 ตรวจสอบความพร้อม", type="primary", use_container_width=True)

if run_clicked:
    if not input_text.strip():
        st.warning("กรุณากรอกข้อมูลก่อน")
    else:
        with st.spinner("AI กำลังตรวจสอบ..."):
            try:
                result = analyze_safety_checklist(input_text)

                st.divider()
                status = result.get("readiness_status", "")
                if status == "Ready":
                    st.success(f"✅ สถานะ: {status}")
                elif status == "Not Ready":
                    st.error(f"⛔ สถานะ: {status}")
                else:
                    st.warning(f"⚠️ สถานะ: {status}")

                missing = result.get("missing_precautions") or []
                if missing:
                    st.markdown("**ข้อควรระวัง/PPE ที่ขาดหายไป:**")
                    for m in missing:
                        st.markdown(f"- {m}")

                st.markdown(f"**สิ่งที่ควรเตรียมก่อนเริ่มงาน:** {result.get('recommended_action')}")

                with st.expander("ดูข้อมูล JSON ต้นฉบับ"):
                    st.json(result)

            except Exception as e:
                st.error(f"เกิดข้อผิดพลาด: {e}")
