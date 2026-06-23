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

# 2. ฟังก์ชันเรียก AI (ให้นักเรียนแก้ Prompt ในส่วนนี้)
def analyze_custom_usecase(user_input):
    
    # TODO: ให้นักเรียนเปลี่ยน Prompt ด้านล่างให้เข้ากับโจทย์ของตนเอง
    prompt = f"""
    You are an AI assistant for ... [ใส่บทบาทของ AI ที่นี่] ...
    Analyze the following text.
    
    Rules:
    - [ใส่กฎข้อที่ 1]
    - [ใส่กฎข้อที่ 2]
    
    Return JSON only with these fields:
    field1, field2, field3
    
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

# 3. สร้างหน้าเว็บด้วย Streamlit (ให้นักเรียนแก้ UI ในส่วนนี้)
st.set_page_config(page_title="My Custom AI App", page_icon="✨")

st.title("✨ My Custom AI Web App")
st.markdown("ระบบวิเคราะห์ข้อมูลอัตโนมัติ (แก้ไขชื่อเรื่องและคำอธิบายตรงนี้)")

# ช่องกรอกข้อมูล
input_text = st.text_area("กรอกข้อมูลที่ต้องการให้ AI ประมวลผล:", height=100)

if st.button("🚀 รัน AI Model", type="primary"):
    if not input_text.strip():
        st.warning("กรุณากรอกข้อมูลก่อน")
    else:
        with st.spinner("AI กำลังทำงาน..."):
            try:
                result = analyze_custom_usecase(input_text)
                
                st.subheader("📊 ผลลัพธ์จาก AI")
                
                # วนลูปดึงค่าตัวแปรทุกตัวจาก JSON ออกมาแสดงผลทีละบรรทัด
                for key, value in result.items():
                    # ปรับชื่อ Key ให้สวยงาม (เช่น my_field -> My Field)
                    formatted_key = key.replace('_', ' ').title()
                    
                    st.markdown(f"##### {formatted_key}")
                    if isinstance(value, dict):
                        # กรณีที่ Value เป็น JSON ซ้อนข้างใน
                        for sub_k, sub_v in value.items():
                            st.info(f"**{sub_k.title()}:** {sub_v}")
                    else:
                        # กรณีทั่วไป ให้แสดงผลในการ์ดสีฟ้า
                        st.info(value)
                        
                # ซ่อน JSON ดิบไว้ใน Expander (เผื่ออยากกดดูโค้ดเบื้องหลัง)
                with st.expander("ดูข้อมูล JSON ต้นฉบับ"):
                    st.json(result)
                             
            except Exception as e:
                st.error(f"เกิดข้อผิดพลาด: {e}")
