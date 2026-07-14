import json
import os
# pyrefly: ignore [missing-import]
import streamlit as st
from dotenv import load_dotenv
from openai import AzureOpenAI

# 1. โหลด Environment Variables
load_dotenv()
client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
)
deployment_name = os.getenv("AZURE_OPENAI_DEPLOYMENT")

# 2. ฟังก์ชันเรียก AI
def analyze_factory_issue(issue_text):
    prompt = f"""
    คุณเป็นผู้ช่วย AI สำหรับจัดการปัญหาในโรงงาน
    วิเคราะห์รายงานปัญหาโรงงาน

    Rules:
    - จัดหมวดหมู่ (category) เป็น Mechanical, Electrical, QA/QC, Safety หรือ Other
    - กำหนดความเร่งด่วน (priority) เป็น Low, Medium หรือ High
    - แนะนำการดำเนินการเร่งด่วนและเครื่องมือที่ต้องเตรียม
    - ร่างข้อความเตือนด้านความปลอดภัยสั้นๆ เป็นภาษาไทย

    ตอบกลับเป็น JSON เท่านั้น โดยมี field ดังนี้:
    summary, category, priority, recommended_action, tools_needed, safety_warning

    รายงานปัญหา:
    {issue_text}
    """
    
    response = client.chat.completions.create(
        model=deployment_name,
        # หมายเหตุ: gpt-5-mini ไม่รองรับ temperature/max_tokens
        # ถ้าใช้ gpt-4o สามารถเพิ่ม temperature=0.0 เพื่อผลลัพธ์ที่คงที่ได้
        messages=[
            {"role": "system", "content": "คุณเป็นผู้ช่วย AI ประจำโรงงาน ตอบกลับเป็น JSON เท่านั้น"},
            {"role": "user", "content": prompt},
        ],
        response_format={ "type": "json_object" }
    )
    return json.loads(response.choices[0].message.content)

# 3. สร้างหน้าเว็บด้วย Streamlit
st.set_page_config(page_title="Factory AI Assistant", page_icon="🏭")

st.title("🏭 BKC Factory AI Assistant")
st.markdown("ระบบวิเคราะห์ปัญหาหน้างาน (Machine, QA, Safety) ด้วย AI")

# ช่องกรอกข้อมูล
issue_input = st.text_area("กรอกข้อมูลปัญหาหน้างานที่พบ:", height=100, 
                           placeholder="เช่น มอเตอร์ปั๊มน้ำมีเสียงดังและมีควันขึ้น")

if st.button("🔍 วิเคราะห์ปัญหาด้วย AI", type="primary"):
    if not issue_input.strip():
        st.warning("กรุณากรอกข้อมูลปัญหาก่อนกดวิเคราะห์")
    else:
        with st.spinner("AI กำลังวิเคราะห์..."):
            try:
                st.session_state["analysis_result"] = analyze_factory_issue(issue_input)
            except Exception as e:
                st.error(f"เกิดข้อผิดพลาดในการเชื่อมต่อ AI: {e}")

# แสดงผลนอกเงื่อนไขปุ่ม "วิเคราะห์" โดยอ่านค่าจาก st.session_state แทนตัวแปรธรรมดา
# เหตุผล: Streamlit รันสคริปต์ใหม่ทั้งไฟล์ทุกครั้งที่มีการโต้ตอบ (เช่น เปลี่ยนค่าใน selectbox ด้านล่าง)
# และ st.button() จะคืนค่า True แค่รอบที่กดเท่านั้น ถ้าเก็บผลลัพธ์ไว้ในตัวแปรธรรมดาในเงื่อนไข if ข้างบน
# ฟอร์มแก้ไขทั้งหมดจะหายไปทันทีที่ผู้ใช้แก้ไขค่าใด ๆ ก่อนกดยืนยัน
if "analysis_result" in st.session_state:
    result = st.session_state["analysis_result"]

    st.subheader("📊 ผลการวิเคราะห์ (Human-in-the-Loop)")
    st.markdown("⚠️ **กรุณาตรวจสอบและแก้ไขผลลัพธ์จาก AI ก่อนกดยืนยันบันทึกลงระบบ**")

    # -------------------------------------------------------------
    # ส่วนแสดงผลแบบ Editable (เพื่อให้คนตรวจสอบก่อน)
    # -------------------------------------------------------------
    priority_list = ["Low", "Medium", "High"]
    ai_priority = result.get("priority", "Low")
    default_index = priority_list.index(ai_priority) if ai_priority in priority_list else 0

    edited_priority = st.selectbox("ระดับความเร่งด่วน:", priority_list, index=default_index)

    col1, col2 = st.columns(2)
    with col1:
        edited_category = st.text_input("หมวดหมู่ปัญหา:", value=result.get('category'))
    with col2:
        edited_tools = st.text_input("เครื่องมือที่ต้องใช้:", value=result.get('tools_needed'))

    edited_summary = st.text_area("สรุปปัญหา:", value=result.get('summary'))
    edited_action = st.text_area("คำแนะนำเบื้องต้น:", value=result.get('recommended_action'))

    edited_warning = st.text_area("ข้อความแจ้งเตือนความปลอดภัย (คัดลอกส่งไลน์ได้):",
                 value=result.get("safety_warning"), height=100)

    st.divider()
    # ปุ่มกดยืนยันหลังจากตรวจสอบแล้ว
    if st.button("✅ ยืนยันข้อมูลและบันทึกลงระบบ (Submit)", type="primary", use_container_width=True):
        # ในการใช้งานจริง โค้ดตรงนี้จะนำตัวแปร edited_... ไปบันทึกลง Database หรือ Excel
        st.success(f"บันทึกข้อมูลเรียบร้อยแล้ว! (หมวดหมู่: {edited_category}, ความเร่งด่วน: {edited_priority})")
