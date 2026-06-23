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
                
                st.subheader("📊 ผลการวิเคราะห์")
                
                # แสดงสีตามระดับความสำคัญ
                priority = result.get("priority", "Low")
                if priority == "High":
                    st.error("🚨 ระดับความเร่งด่วน: สูงสุด (High) - แจ้งหัวหน้างานทันที!")
                elif priority == "Medium":
                    st.warning("⚠️ ระดับความเร่งด่วน: ปานกลาง (Medium) - เตรียมการเข้าแก้ไข")
                else:
                    st.success("✅ ระดับความเร่งด่วน: ปกติ (Low)")
                    
                # ใช้คอลัมน์เพื่อจัดหน้าให้สวยงาม
                col1, col2 = st.columns(2)
                with col1:
                    st.info(f"**หมวดหมู่ปัญหา:** {result.get('category')}")
                with col2:
                    st.info(f"**เครื่องมือที่ต้องใช้:** {result.get('tools_needed')}")
                    
                st.write(f"**สรุปปัญหา:** {result.get('summary')}")
                st.write(f"**คำแนะนำเบื้องต้น:** {result.get('recommended_action')}")
                
                # กล่องข้อความแจ้งเตือน (สามารถคัดลอกได้ง่าย)
                st.text_area("ข้อความแจ้งเตือนความปลอดภัย (คัดลอกส่งไลน์ได้):", 
                             result.get("safety_warning"), height=100)
                             
            except Exception as e:
                st.error(f"เกิดข้อผิดพลาดในการเชื่อมต่อ AI: {e}")
