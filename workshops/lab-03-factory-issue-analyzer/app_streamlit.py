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
    You are an AI assistant for factory issue management.
    Analyze the factory issue report.
    
    Rules:
    - Classify category as Mechanical, Electrical, QA/QC, Safety/EHS, or Other.
    - Set priority as Low, Medium, or High.
    - Recommend immediate action and tools to prepare.
    - Draft a short safety warning in Thai.
    
    Return JSON only with these fields:
    summary, category, priority, recommended_action, tools_needed, safety_warning
    
    Issue report:
    {issue_text}
    """
    
    response = client.chat.completions.create(
        model=deployment_name,
        temperature=0.0,
        messages=[
            {"role": "system", "content": "You are a factory AI assistant. Return JSON only."},
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
                result = analyze_factory_issue(issue_input)
                
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
                             
            except Exception as e:
                st.error(f"เกิดข้อผิดพลาดในการเชื่อมต่อ AI: {e}")
