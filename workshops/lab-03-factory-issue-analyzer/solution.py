import json
import os
from datetime import datetime
from dotenv import load_dotenv
from openai import AzureOpenAI

load_dotenv()

client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
)

deployment_name = os.getenv("AZURE_OPENAI_DEPLOYMENT")

def analyze_issue(case_id: str, issue_report: str) -> dict:
    prompt = f"""
    You are an AI assistant for factory issue management.

    Analyze the factory issue report.

    Rules:
    - Classify category as Mechanical, Electrical, QA/QC, Safety, or Other.
    - Set priority as Low, Medium, or High.
    - Recommend immediate action and tools to prepare.
    - Draft a short safety warning in Thai.

    Return JSON only with these fields:
    summary, category, priority, recommended_action, tools_needed, safety_warning

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
    result = json.loads(response.choices[0].message.content)
    result["case_id"] = case_id
    result["analyzed_at"] = datetime.now().strftime("%Y-%m-%d %H:%M")
    return result

def get_routing_action(priority: str) -> str:
    if priority == "High":
        return "แจ้งหัวหน้ากะทันที + สั่งหยุดเครื่องชั่วคราว (ถ้าจำเป็น)"
    elif priority == "Medium":
        return "สร้างใบแจ้งซ่อม (Work Order) + ลงพื้นที่ตรวจสอบภายใน 2 ชม."
    return "บันทึกใน Log ประจำวัน + ตรวจสอบในรอบถัดไป"

# Load cases from sample data
with open("../../sample-data/factory_issues.json", encoding="utf-8") as f:
    cases = json.load(f)

all_results = []

for case in cases[:3]: # ทดสอบ 3 เคสแรก
    print(f"\n{'='*50}")
    print(f"Processing {case['case_id']}...")
    print(f"Input: {case['issue_report'].strip()}")

    result = analyze_issue(case["case_id"], case["issue_report"])
    all_results.append(result)

    print(f"\n  Category : {result.get('category')}")
    print(f"  Priority : {result.get('priority')}")
    print(f"  Summary  : {result.get('summary')}")
    print(f"  Tools    : {result.get('tools_needed')}")
    print(f"  Action   : {result.get('recommended_action')}")
    print(f"\n  Routing  --> {get_routing_action(result.get('priority', 'Low'))}")

output_path = "factory_issues_output.json"
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(all_results, f, ensure_ascii=False, indent=2)

print(f"\nResults saved to {output_path}")
