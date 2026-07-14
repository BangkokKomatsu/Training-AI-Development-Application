import json
import os
import time
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

def analyze_issue(issue_report: str) -> dict:
    # TODO 1: เพิ่มกฎอีก 2 ข้อในส่วน Rules ด้านล่าง (แทนที่บรรทัด "[TODO 1: ...]" ทั้งสองบรรทัด)
    # แล้วเพิ่มชื่อ field ใหม่ 2 ตัวต่อท้ายบรรทัด "category, priority, summary" ด้วย
    # -> missing_information, confidence
    # ใบ้: ดูเฉลยเต็มได้จาก app_streamlit.py ในโฟลเดอร์นี้ (มี field พวกนี้อยู่แล้ว) หรือ solution.py
    prompt = f"""
    คุณเป็นผู้ช่วย AI สำหรับจัดการปัญหาในโรงงาน
    วิเคราะห์รายงานปัญหาโรงงาน

    Rules:
    - จัดหมวดหมู่ (category) เป็น Mechanical, Electrical, QA/QC, Safety หรือ Other
    - กำหนดความเร่งด่วน (priority) เป็น Low, Medium หรือ High
    - [TODO 1: เพิ่มกฎเรื่อง missing_information ที่นี่]
    - [TODO 1: เพิ่มกฎเรื่อง confidence ที่นี่]

    ตอบกลับเป็น JSON เท่านั้น โดยมี field ดังนี้:
    category, priority, summary

    รายงานปัญหา:
    {issue_report}
    """
    try:
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
    except Exception as e:
        print(f"  [Error] เกิดข้อผิดพลาดในการเรียก AI หรือแปลง JSON: {e}")
        return {
            "category": "Error: Needs Manual Review",
            "priority": "Unknown",
            "summary": "AI processing failed"
        }

# TODO 2: เขียนฟังก์ชัน get_action_required(priority) ที่รับค่า priority ("High"/"Medium"/อื่นๆ)
# แล้ว return ข้อความว่าควรทำอะไรต่อ (ใบ้: ใช้ if/elif/else)
# def get_action_required(priority: str) -> str:
#     if priority == "High":
#         return "แจ้งหัวหน้ากะทันที"
#     elif priority == "Medium":
#         return "สร้างใบแจ้งซ่อมภายใน 24 ชม."
#     return "บันทึก Log ตรวจสอบในรอบถัดไป"

# 1. โหลดข้อมูลจากไฟล์ JSON (สมมุติว่าเป็นข้อมูลที่ดึงมาจากระบบ ERP หรือตาราง)
with open("../../sample-data/factory_issues.json", encoding="utf-8") as f:
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
    results.append({
        "Category": ai_result.get("category"),
        "Priority": ai_result.get("priority"),
        "Summary": ai_result.get("summary"),
        # TODO 1 (ต่อ): ดึง missing_information และ confidence จาก ai_result มาใส่เป็นคอลัมน์ใหม่
        # "Missing_Info": ai_result.get("missing_information"),
        # "Confidence": ai_result.get("confidence"),
        # TODO 2 (ต่อ): เรียก get_action_required(...) แล้วใส่ผลลัพธ์เป็นคอลัมน์ "Action_Required"
        # "Action_Required": get_action_required(ai_result.get("priority")),
    })
    time.sleep(1)  # กันชน Rate Limit (RPM/TPM) เวลาหลายคนรันพร้อมกัน — ดู docs/03-token-basics.md

# 3. นำผลลัพธ์มาต่อเข้ากับ DataFrame เดิม
result_df = pd.DataFrame(results)
df = pd.concat([df, result_df], axis=1)

# 4. บันทึกลงไฟล์ Excel
output_file = "factory_issues_analyzed.xlsx"
df.to_excel(output_file, index=False)

print(f"\nประมวลผลเสร็จสิ้น! บันทึกผลลัพธ์ลงไฟล์ {output_file} เรียบร้อยแล้ว")
# TODO 3: ลองเปิดไฟล์ Excel เพื่อดูผลลัพธ์ และเช็คว่าคอลัมน์ Missing_Info, Confidence, Action_Required
# ที่เพิ่มเข้ามาใน TODO 1-2 แสดงถูกต้องหรือไม่ (เทียบเฉลยได้จาก solution.py)
