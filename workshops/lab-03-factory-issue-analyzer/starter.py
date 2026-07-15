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
มอเตอร์ปั๊มน้ำหล่อเย็นไลน์ผลิต 2 มีเสียงดังผิดปกติและมีควันขึ้นเล็กน้อยที่บริเวณขั้วต่อสายไฟ ยังไม่ได้ปิดเครื่อง
"""

prompt = f"""
คุณเป็นผู้ช่วย AI สำหรับจัดการปัญหาในโรงงาน

วิเคราะห์รายงานปัญหาโรงงานด้านล่างนี้

Rules:
- จัดหมวดหมู่ (category) เป็น Mechanical, Electrical, QA/QC, Safety หรือ Other
- กำหนดความเร่งด่วน (priority) เป็น Low, Medium หรือ High
- [TODO 1: เพิ่มกฎเรื่องการแนะนำการดำเนินการเร่งด่วนและเครื่องมือที่ต้องเตรียม ที่นี่]
- [TODO 2: เพิ่มกฎเรื่องการร่างข้อความเตือนด้านความปลอดภัยสั้นๆ เป็นภาษาไทย ที่นี่]

ตอบกลับเป็น JSON เท่านั้น โดยมี field ดังนี้:
summary, category, priority

รายงานปัญหา:
{issue_report}
"""

response = client.chat.completions.create(
    model=deployment_name,
    messages=[
        {"role": "system", "content": "คุณเป็นผู้ช่วย AI ประจำโรงงาน ตอบกลับเป็น JSON เท่านั้น"},
        {"role": "user", "content": prompt},
    ],
    response_format={ "type": "json_object" } # บังคับให้ AI ตอบเป็น JSON เสมอ
)

# Step 1: Parse JSON
result = json.loads(response.choices[0].message.content)

# Step 2: แสดง field แต่ละตัว
print("=== Factory Issue Analysis ===")
print(f"Category  : {result.get('category')}")
print(f"Priority  : {result.get('priority')}")
print(f"Summary   : {result.get('summary')}")
