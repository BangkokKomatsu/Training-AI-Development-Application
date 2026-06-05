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
You are an AI assistant for supplier issue management at BKC.

Analyze the supplier issue report.

Rules:
- Do not assume missing information.
- If information is missing, list it clearly.
- Classify category as Quality, Delivery, Document, IT, Commercial, or Other.
- Set priority as Low, Medium, or High.
- Recommend next action.
- Draft a professional email reply in English.

Return JSON only with these fields:
summary, category, priority, missing_information, recommended_action, email_reply

Issue report:
{issue_report}
"""
    response = client.chat.completions.create(
        model=deployment_name,
        messages=[
            {"role": "system", "content": "You are a business AI assistant. Return JSON only."},
            {"role": "user", "content": prompt},
        ],
    )
    result = json.loads(response.choices[0].message.content)
    result["case_id"] = case_id
    result["analyzed_at"] = datetime.now().strftime("%Y-%m-%d %H:%M")
    return result


def get_routing_action(priority: str) -> str:
    if priority == "High":
        return "แจ้ง Procurement Manager ทันที + สร้าง Escalation Case"
    elif priority == "Medium":
        return "สร้าง Ticket ใน ERP + ติดตามภายใน 24 ชั่วโมง"
    return "บันทึกใน Log + ติดตามตาม SLA ปกติ"


# Load cases from sample data
with open("sample-data/supplier_issues.json", encoding="utf-8") as f:
    cases = json.load(f)

all_results = []

for case in cases:
    print(f"\n{'='*50}")
    print(f"Processing {case['case_id']}...")
    print(f"Input: {case['issue_report'].strip()}")

    result = analyze_issue(case["case_id"], case["issue_report"])
    all_results.append(result)

    print(f"\n  Category : {result['category']}")
    print(f"  Priority : {result['priority']}")
    print(f"  Summary  : {result['summary']}")
    print(f"  Missing  : {result.get('missing_information', '-')}")
    print(f"  Action   : {result['recommended_action']}")
    print(f"\n  Routing  --> {get_routing_action(result['priority'])}")
    print(f"\n  --- Email Draft (copy & send) ---")
    print(result.get("email_reply", ""))
    print(f"  --------------------------------")

# Save all results to JSON (สมมุติส่งต่อ ERP หรือ dashboard)
output_path = "supplier_issues_output.json"
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(all_results, f, ensure_ascii=False, indent=2)

# Summary
print(f"\n{'='*50}")
print("=== Batch Summary ===")
print(f"Total cases analyzed : {len(all_results)}")
high = sum(1 for r in all_results if r["priority"] == "High")
medium = sum(1 for r in all_results if r["priority"] == "Medium")
low = sum(1 for r in all_results if r["priority"] == "Low")
print(f"  High   : {high} case(s) — Escalate immediately")
print(f"  Medium : {medium} case(s) — Follow up in 24h")
print(f"  Low    : {low} case(s) — Log and monitor")
print(f"\nResults saved to {output_path}")
