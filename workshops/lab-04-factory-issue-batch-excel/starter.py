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
    prompt = f"""
    You are an AI assistant for factory issue management.
    Analyze the factory issue report.

    Rules:
    - Classify category as Mechanical, Electrical, QA/QC, Safety/EHS, or Other.
    - Set priority as Low, Medium, or High.

    Return JSON only with these fields:
    category, priority, summary

    Issue report:
    {issue_report}
    """
    try:
        response = client.chat.completions.create(
            model=deployment_name,
            # หมายเหตุ: gpt-5-mini ไม่รองรับ temperature/max_tokens
            # ถ้าใช้ gpt-4o สามารถเพิ่ม temperature=0.0 เพื่อผลลัพธ์ที่คงที่ได้
            messages=[
                {"role": "system", "content": "You are a factory AI assistant. Return JSON only."},
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
        "Summary": ai_result.get("summary")
    })
    time.sleep(1)  # กันชน Rate Limit (RPM/TPM) เวลาหลายคนรันพร้อมกัน — ดู docs/03-token-basics.md

# 3. นำผลลัพธ์มาต่อเข้ากับ DataFrame เดิม
result_df = pd.DataFrame(results)
df = pd.concat([df, result_df], axis=1)

# 4. บันทึกลงไฟล์ Excel
output_file = "factory_issues_analyzed.xlsx"
df.to_excel(output_file, index=False)

print(f"\nประมวลผลเสร็จสิ้น! บันทึกผลลัพธ์ลงไฟล์ {output_file} เรียบร้อยแล้ว")
# TODO: ลองเปิดไฟล์ Excel เพื่อดูผลลัพธ์
