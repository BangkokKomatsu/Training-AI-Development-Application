import json
import os
import time
from pathlib import Path
import pandas as pd
from dotenv import load_dotenv
from openai import AzureOpenAI

load_dotenv()

client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
)

deployment_name = os.getenv("AZURE_OPENAI_DEPLOYMENT")

BASE_DIR = Path(__file__).resolve().parent

def analyze_issue(issue_report: str) -> dict:
    prompt = f"""
    คุณเป็นผู้ช่วย AI สำหรับจัดการปัญหาในโรงงาน
    วิเคราะห์รายงานปัญหาโรงงาน

    Rules:
    - จัดหมวดหมู่ (category) เป็น Mechanical, Electrical, QA/QC, Safety หรือ Other
    - กำหนดความเร่งด่วน (priority) เป็น Low, Medium หรือ High
    - ระบุสิ่งที่จำเป็นต่อการจัดหมวดหมู่ปัญหานี้อย่างมั่นใจแต่ขาดหายไปจากข้อมูลนำเข้า
      ไว้ใน field "missing_information" (list ว่างได้ถ้าไม่มีอะไรขาด)
    - เพิ่ม field "confidence": High, Medium หรือ Low ตามความครบถ้วนของข้อมูลนำเข้า

    ตอบกลับเป็น JSON เท่านั้น โดยมี field ดังนี้:
    category, priority, summary, missing_information, confidence

    รายงานปัญหา:
    {issue_report}
    """
    try:
        response = client.chat.completions.create(
            model=deployment_name,
            messages=[
                {"role": "system", "content": "คุณเป็นผู้ช่วย AI ประจำโรงงาน ตอบกลับเป็น JSON เท่านั้น"},
                {"role": "user", "content": prompt},
            ],
            response_format={ "type": "json_object" }
        )
        return json.loads(response.choices[0].message.content)
    except Exception as e:
        print(f"  [Error] เกิดข้อผิดพลาดในการเรียก AI หรือแปลง JSON: {e}")
        return {
            "category": "Error: Needs Manual Review",
            "priority": "Unknown",
            "summary": "AI processing failed",
            "missing_information": [],
            "confidence": "Unknown"
        }

def get_action_required(priority: str) -> str:
    if priority == "High":
        return "แจ้งหัวหน้ากะทันที"
    elif priority == "Medium":
        return "สร้างใบแจ้งซ่อมภายใน 24 ชม."
    return "บันทึก Log ตรวจสอบในรอบถัดไป"

# 1. โหลดข้อมูลจากไฟล์ JSON (สมมุติว่าเป็นข้อมูลที่ดึงมาจากระบบ ERP หรือตาราง)
with open(BASE_DIR / "../../sample-data/factory_issues.json", encoding="utf-8") as f:
    data = json.load(f)

# แปลงเป็น DataFrame ของ Pandas
df = pd.DataFrame(data)
print("ข้อมูลก่อนประมวลผล:")
print(df.head())

# 2. วนลูปส่งให้ AI วิเคราะห์
results = []
for index, row in df.iterrows():
    print(f"\nProcessing Case ID: {row['case_id']}...")
    ai_result = analyze_issue(row['issue_report'])
    missing_info = ai_result.get("missing_information") or []
    results.append({
        "Category": ai_result.get("category"),
        "Priority": ai_result.get("priority"),
        "Summary": ai_result.get("summary"),
        "Missing_Info": ", ".join(missing_info) if isinstance(missing_info, list) else missing_info,
        "Confidence": ai_result.get("confidence"),
        "Action_Required": get_action_required(ai_result.get("priority")),
    })
    time.sleep(1)  # กันชน Rate Limit (RPM/TPM) เวลาหลายคนรันพร้อมกัน — ดู docs/03-token-basics.md

# 3. นำผลลัพธ์มาต่อเข้ากับ DataFrame เดิม
result_df = pd.DataFrame(results)
df = pd.concat([df, result_df], axis=1)

# 4. บันทึกลงไฟล์ Excel
output_file = BASE_DIR / "factory_issues_analyzed.xlsx"
df.to_excel(output_file, index=False)

print(f"\nประมวลผลเสร็จสิ้น! บันทึกผลลัพธ์ลงไฟล์ {output_file} เรียบร้อยแล้ว")
