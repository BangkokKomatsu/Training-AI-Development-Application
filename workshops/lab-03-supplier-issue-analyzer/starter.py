import json
import os
from dotenv import load_dotenv
from openai import AzureOpenAI

load_dotenv()

client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
)

deployment_name = os.getenv("AZURE_OPENAI_DEPLOYMENT")

issue_report = """
Supplier ABC แจ้งว่าสินค้าล็อตล่าสุดมีรอยขีดข่วนหลายชิ้น
แต่ยังไม่ได้แจ้ง lot number และยังไม่ได้แนบรูปภาพ
"""

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

# Step 1: Parse JSON
result = json.loads(response.choices[0].message.content)

# Step 2: แสดง field แต่ละตัว
print("=== Supplier Issue Analysis ===")
print(f"Category  : {result['category']}")
print(f"Priority  : {result['priority']}")
print(f"Summary   : {result['summary']}")
print(f"Missing   : {result.get('missing_information', '-')}")
print(f"Action    : {result['recommended_action']}")

# Step 3: แสดง Email Draft ที่พร้อม copy-paste ส่งกลับ supplier
print("\n=== Email Draft (ready to send) ===")
print(result.get("email_reply", ""))

# TODO: ลองเพิ่ม routing ตาม priority
# if result["priority"] == "High":
#     print("แจ้ง Procurement Manager ทันที")

# TODO: ลองบันทึกผลลัพธ์ลงไฟล์
# with open("supplier_result.json", "w", encoding="utf-8") as f:
#     json.dump(result, f, ensure_ascii=False, indent=2)
