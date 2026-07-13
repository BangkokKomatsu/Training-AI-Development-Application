import json
import os
import time
import pandas as pd
import streamlit as st
from dotenv import load_dotenv
from openai import AzureOpenAI
import io

# 1. โหลด Environment Variables
load_dotenv()
client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
)
deployment_name = os.getenv("AZURE_OPENAI_DEPLOYMENT")

# 2. ฟังก์ชันวิเคราะห์ปัญหา
def analyze_issue(issue_report):
    prompt = f"""
    You are an AI assistant for factory issue management.
    Analyze the factory issue report.

    Rules:
    - Do not assume or invent any information that is not in the input.
    - Choose category only from: Mechanical, Electrical, QA/QC, Safety/EHS, Other.
    - Set priority as Low, Medium, or High. If the input does not give enough detail to
      determine priority, use "Unknown" instead of guessing.
    - List anything needed to classify this issue confidently but missing from the input
      in the "missing_information" field (empty list if nothing is missing).
    - Add a "confidence" field: High, Medium, or Low, based on how complete the input is.

    Return JSON only with these fields:
    category, priority, summary, missing_information, confidence

    Issue report:
    {issue_report}
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

# 3. หน้าเว็บ Streamlit
st.set_page_config(page_title="Factory Batch Processor", page_icon="📑")
st.title("📑 AI Excel Batch Processor")
st.markdown("ระบบอัปโหลดไฟล์ Excel ปัญหาโรงงาน เพื่อให้ AI ช่วยคัดแยกหมวดหมู่และจัดลำดับความสำคัญอัตโนมัติ")

uploaded_file = st.file_uploader("อัปโหลดไฟล์รายงานปัญหา (Excel / CSV)", type=['xlsx', 'csv'])

if uploaded_file is not None:
    # อ่านไฟล์ที่อัปโหลด
    if uploaded_file.name.endswith('.csv'):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)
        
    st.write("ข้อมูลก่อนประมวลผล:")
    st.dataframe(df.head())
    
    if st.button("🚀 เริ่มการวิเคราะห์ข้อมูลด้วย AI", type="primary"):
        # เตรียม Progress Bar
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        results = []
        total_rows = len(df)
        
        # วนลูปวิเคราะห์ทีละบรรทัด
        for index, row in df.iterrows():
            status_text.text(f"กำลังประมวลผลบรรทัดที่ {index + 1} จาก {total_rows}...")
            
            # สมมุติว่าในไฟล์มีคอลัมน์ชื่อ 'issue_report'
            report_text = row.get('issue_report', str(row.values)) 
            
            try:
                ai_result = analyze_issue(report_text)
                missing_info = ai_result.get("missing_information") or []
                results.append({
                    "AI_Category": ai_result.get("category"),
                    "AI_Priority": ai_result.get("priority"),
                    "AI_Summary": ai_result.get("summary"),
                    "AI_Missing_Info": ", ".join(missing_info) if isinstance(missing_info, list) else missing_info,
                    "AI_Confidence": ai_result.get("confidence")
                })
            except Exception as e:
                results.append({
                    "AI_Category": "Error", "AI_Priority": "Error", "AI_Summary": str(e),
                    "AI_Missing_Info": "", "AI_Confidence": ""
                })

            time.sleep(1)  # กันชน Rate Limit เวลาหลายคนรันพร้อมกัน

            # อัปเดต Progress Bar
            progress_bar.progress((index + 1) / total_rows)
            
        status_text.text("ประมวลผลเสร็จสมบูรณ์! 🎉")
        
        # นำผลลัพธ์มารวมกับ DataFrame เดิม
        result_df = pd.DataFrame(results)
        final_df = pd.concat([df, result_df], axis=1)
        
        st.write("ข้อมูลหลังประมวลผล:")
        st.dataframe(final_df)
        
        # สร้างไฟล์ Excel บนหน่วยความจำสำหรับให้ดาวน์โหลด
        buffer = io.BytesIO()
        with pd.ExcelWriter(buffer, engine='openpyxl') as writer:
            final_df.to_excel(writer, index=False)
        
        st.download_button(
            label="📥 ดาวน์โหลดไฟล์ Excel ผลลัพธ์",
            data=buffer.getvalue(),
            file_name="factory_issues_analyzed.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
