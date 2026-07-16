# ตัวอย่างอ้างอิง (Reference Example) - งานโลจิสติกส์และคลังสินค้า
# เปิดไฟล์นี้ดูเป็นแนวทางก่อนเริ่มออกแบบ Use Case ของตัวเองใน app_streamlit_template.py
# ไม่ใช่หนึ่งใน 5 หัวข้อที่ต้องเลือกใน README (ดู README.md)
#
# หมายเหตุ: ตัวอย่างนี้เน้น "ตรวจสอบความพร้อมก่อนบันทึกรับสินค้าเข้าสต๊อก" (goods receiving check)
# ซึ่งเป็นคนละมุมกับตัวเลือกข้อ 4 ในลิสต์ Mini Challenge ("Logistics Delay Summarizer" ที่สรุปปัญหา
# สินค้าล่าช้าที่เกิดขึ้นแล้ว) ดังนั้นยังเลือกทำหัวข้อ Logistics Delay Summarizer เป็น mini challenge ของ
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

def analyze_goods_receipt(user_input):
    prompt = f"""
    คุณเป็นผู้ช่วย AI สำหรับฝ่ายโลจิสติกส์และคลังสินค้า (Logistics & Warehouse)

    Task:
    ตรวจสอบบันทึกการรับสินค้าเข้าคลังแบบไม่เป็นทางการ (ที่พนักงานคลังเขียนตอนรับของ)
    ว่าพร้อมบันทึกรับเข้าสต๊อกในระบบหรือไม่

    Context:
    พนักงานคลังมักเขียนบันทึกสั้นๆ ตอนรับสินค้าเข้า (จำนวนที่ได้รับ, สภาพสินค้า) ก่อนที่จะกรอกเข้าระบบ
    WMS/ERP อย่างเป็นทางการ ต้องเช็คว่าจำนวนที่ได้รับตรงกับที่สั่งไหม และมีความเสียหายไหม ก่อนบันทึก
    รับเข้าสต๊อก

    Rules:
    - ห้ามเดาข้อมูลใดๆ ที่ไม่ได้ระบุไว้ในข้อมูลนำเข้า
    - ถ้าจำนวนที่ได้รับไม่ตรงกับจำนวนที่สั่ง ให้ระบุส่วนต่างไว้ใน field "quantity_discrepancy"
      (ระบุ "None" ถ้าไม่มีการระบุจำนวนที่สั่ง หรือจำนวนตรงกัน)
    - ระบุความเสียหายหรือปัญหาสภาพสินค้าที่พบ ถ้ามี (ระบุ "None" ถ้าไม่มี)
    - แนะนำขั้นตอนถัดไปก่อนบันทึกรับเข้าสต๊อก
      (เช่น ต้องแจ้ง Supplier, ต้องถ่ายรูปหลักฐาน, ต้องแยกของเสียออกก่อนนับ)

    Output format:
    ตอบกลับเป็น JSON เท่านั้น โดยมี field ดังนี้:
    - receiving_status: "Ready to Stock" or "Needs Review"
    - quantity_discrepancy: ข้อความอธิบายส่วนต่างจำนวน (string, ระบุ "None" ถ้าไม่มี)
    - damage_note: ข้อความอธิบายความเสียหายที่พบ (string, ระบุ "None" ถ้าไม่มี)
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

st.set_page_config(page_title="Goods Receiving Checker", page_icon="📦", layout="centered")
st.title("📦 Goods Receiving Checker")
st.caption("ตัวอย่างอ้างอิง: AI ช่วยตรวจสอบบันทึกรับสินค้าเข้าคลังก่อนบันทึกเข้าสต๊อก")
st.divider()

with st.container(border=True):
    input_text = st.text_area(
        "วางบันทึกการรับสินค้าเข้าคลังที่ต้องการให้ AI ตรวจสอบ:",
        height=120,
        placeholder="เช่น: รับน้ำมันไฮดรอลิกเข้าคลัง สั่งไป 20 ถัง แต่ได้รับมาแค่ 18 ถัง มี 2 ถังมีรอยรั่วที่ฝา ยังไม่ได้แจ้ง Supplier",
    )
    run_clicked = st.button("🚀 ตรวจสอบการรับสินค้า", type="primary", use_container_width=True)

if run_clicked:
    if not input_text.strip():
        st.warning("กรุณากรอกข้อมูลก่อน")
    else:
        with st.spinner("AI กำลังตรวจสอบ..."):
            try:
                result = analyze_goods_receipt(input_text)

                st.divider()
                status = result.get("receiving_status", "")
                if status == "Ready to Stock":
                    st.success(f"✅ สถานะ: {status}")
                else:
                    st.warning(f"⚠️ สถานะ: {status}")

                discrepancy = result.get("quantity_discrepancy")
                if discrepancy and discrepancy != "None":
                    st.error(f"📉 จำนวนไม่ตรงกัน: {discrepancy}")

                damage = result.get("damage_note")
                if damage and damage != "None":
                    st.warning(f"⚠️ ความเสียหาย: {damage}")

                st.markdown(f"**ขั้นตอนถัดไป:** {result.get('recommended_next_step')}")

                with st.expander("ดูข้อมูล JSON ต้นฉบับ"):
                    st.json(result)

            except Exception as e:
                st.error(f"เกิดข้อผิดพลาด: {e}")
