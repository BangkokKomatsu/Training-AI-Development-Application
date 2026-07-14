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
    คุณเป็นผู้ช่วย AI สำหรับฝ่ายซ่อมบำรุง (Maintenance)
    หน้าที่ของคุณคือแปลงคำขอแจ้งซ่อมแบบไม่เป็นทางการ (ที่พนักงานโรงงานเขียน) ให้เป็นใบสั่งงานซ่อม (work order) ที่มีโครงสร้าง
    วิเคราะห์ข้อความต่อไปนี้

    Rules:
    - [ใส่กฎข้อที่ 1]
    - [ใส่กฎข้อที่ 2]

    ตอบกลับเป็น JSON เท่านั้น โดยมี field ดังนี้:
    - work_order_title: สรุปหัวข้องานซ่อมแบบสั้น กระชับ
    - equipment_or_location: เครื่องจักรหรือสถานที่ที่เกี่ยวข้อง
    - priority: ระดับความเร่งด่วน (High, Medium, Low)
    - problem_description: อธิบายปัญหาที่พบโดยละเอียด
    - recommended_action: ข้อเสนอแนะขั้นตอนการซ่อม/แก้ไขเบื้องต้น

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

# 3. ตกแต่งหน้าเว็บด้วย Streamlit (ให้นักเรียนแก้ UI ในส่วนนี้)
st.set_page_config(page_title="My Custom AI App", page_icon="✨", layout="centered")

# ธีมสี/ฟอนต์ของหน้าเว็บ (ปรับสีได้ตามใจ ไม่จำเป็นต้องเข้าใจ CSS ทั้งหมดก็แก้ไขได้)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+Thai:wght@400;500;600;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Noto Sans Thai', sans-serif;
    }
    div[data-testid="stButton"] > button {
        background-color: #1E3A5F;
        color: #FFFFFF;
        border-radius: 8px;
        border: none;
        padding: 0.6rem 1.5rem;
        font-weight: 600;
        transition: background-color 150ms ease;
    }
    div[data-testid="stButton"] > button:hover {
        background-color: #2563EB;
        color: #FFFFFF;
    }
</style>
""", unsafe_allow_html=True)

# หัวข้อหน้าเว็บ
st.title("✨ My Custom AI Web App")
st.caption("ระบบวิเคราะห์ข้อมูลอัตโนมัติ (แก้ไขชื่อเรื่องและคำอธิบายตรงนี้)")
st.divider()

# ช่องกรอกข้อมูล (ใส่กรอบการ์ดให้ดูเป็นสัดส่วน)
with st.container(border=True):
    input_text = st.text_area(
        "กรอกข้อมูลที่ต้องการให้ AI ประมวลผล:",
        height=120,
        placeholder="เช่น พิมพ์ปัญหา/ข้อความที่ต้องการให้ AI วิเคราะห์ที่นี่...",
    )
    run_clicked = st.button("🚀 รัน AI Model", type="primary", use_container_width=True)

if run_clicked:
    if not input_text.strip():
        st.warning("กรุณากรอกข้อมูลก่อน")
    else:
        with st.spinner("AI กำลังทำงาน..."):
            try:
                result = analyze_custom_usecase(input_text)

                st.divider()
                st.subheader("📊 ผลลัพธ์จาก AI")

                # แสดงระดับความเร่งด่วนเป็นจุดสี (ถ้า field นี้มีอยู่ในผลลัพธ์)
                PRIORITY_DOT = {"high": "🔴", "medium": "🟡", "low": "🟢"}

                # วนลูปดึงค่าตัวแปรทุกตัวจาก JSON มาแสดงผลทีละใบการ์ด
                for key, value in result.items():
                    # ปรับชื่อ Key ให้สวยงาม (เช่น my_field -> My Field)
                    formatted_key = key.replace('_', ' ').title()

                    with st.container(border=True):
                        if isinstance(value, dict):
                            # กรณีที่ Value เป็น JSON ซ้อนข้างใน
                            st.markdown(f"**{formatted_key}**")
                            for sub_k, sub_v in value.items():
                                st.markdown(f"- **{sub_k.title()}:** {sub_v}")
                        elif key.lower() == "priority" and str(value).lower() in PRIORITY_DOT:
                            dot = PRIORITY_DOT[str(value).lower()]
                            st.markdown(f"**{formatted_key}:** {dot} {value}")
                        else:
                            # กรณีทั่วไป
                            st.markdown(f"**{formatted_key}**")
                            st.write(value)

                # ซ่อน JSON ดิบไว้ใน Expander (เผื่ออยากกดดูโค้ดเบื้องหลัง)
                with st.expander("ดูข้อมูล JSON ต้นฉบับ"):
                    st.json(result)

            except Exception as e:
                st.error(f"เกิดข้อผิดพลาด: {e}")
