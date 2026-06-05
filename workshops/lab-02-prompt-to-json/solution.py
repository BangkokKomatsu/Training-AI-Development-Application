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

issue_report = "Supplier XYZ แจ้งว่าส่งของล่าช้า 3 วัน เพราะเครื่องจักรเสีย และยังไม่ยืนยันวันส่งใหม่"

prompt = f"""
You are an AI assistant for supplier issue management at BKC.

Analyze the issue report below.

Rules:
- Do not assume missing information.
- If information is missing, list it clearly.
- Classify the issue as Quality, Delivery, Document, IT, Commercial, or Other.
- Set priority as Low, Medium, or High.

Return JSON only with these fields:
summary, category, priority, missing_information, recommended_action

Issue report:
{issue_report}
"""

response = client.chat.completions.create(
    model=deployment_name,
    messages=[
        {"role": "system", "content": "You return concise and valid JSON only."},
        {"role": "user", "content": prompt},
    ],
)

# Step 1: Parse JSON จาก AI
result = json.loads(response.choices[0].message.content)

# Step 2: แสดง field แต่ละตัวแบบอ่านง่าย
print("=== AI Analysis Result ===")
print(f"Summary   : {result['summary']}")
print(f"Category  : {result['category']}")
print(f"Priority  : {result['priority']}")
print(f"Missing   : {result.get('missing_information', '-')}")
print(f"Action    : {result['recommended_action']}")

# Step 3: ใช้ priority field ตัดสินใจทำสิ่งต่อไป
print("\n=== Routing Decision ===")
if result["priority"] == "High":
    print("HIGH PRIORITY — แจ้ง Procurement Manager ทันที")
elif result["priority"] == "Medium":
    print("MEDIUM — สร้าง Ticket ใน ERP ติดตามใน 24 ชั่วโมง")
else:
    print("LOW — บันทึกไว้ติดตามตาม SLA ปกติ")

# Step 4: บันทึก JSON ลงไฟล์ (สมมุติว่าส่งต่อระบบอื่น เช่น ERP, dashboard)
with open("lab02_output.json", "w", encoding="utf-8") as f:
    json.dump(result, f, ensure_ascii=False, indent=2)

print("\nSaved to lab02_output.json — พร้อมส่งต่อระบบอื่น")
