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
คุณเป็นผู้ช่วย AI สำหรับจัดการปัญหา Supplier ของ BKC

วิเคราะห์รายงานปัญหาด้านล่างนี้

Rules:
- ห้ามเดาข้อมูลที่ขาดหายไป
- ถ้าข้อมูลขาดหายไป ให้ระบุให้ชัดเจน
- จัดหมวดหมู่ปัญหาเป็น Quality, Delivery, Document, IT, Commercial หรือ Other
- กำหนดความเร่งด่วน (priority) เป็น Low, Medium หรือ High

ตอบกลับเป็น JSON เท่านั้น โดยมี field ดังนี้:
summary, category, priority, missing_information, recommended_action

รายงานปัญหา:
{issue_report}
"""

# response_format={"type": "json_object"} บังคับให้ AI ตอบกลับเป็น JSON string ล้วน ๆ
# (ไม่มีข้อความอื่นปน) — ทำให้ json.loads() ด้านล่างแปลงเป็น dict ได้แน่นอน
# เงื่อนไข: ต้องมีคำว่า "JSON" อยู่ใน prompt ด้วย ไม่งั้น Azure OpenAI จะ error
response = client.chat.completions.create(
    model=deployment_name,
    messages=[
        {"role": "system", "content": "คุณตอบกลับเป็น JSON ที่ถูกต้องและกระชับเท่านั้น"},
        {"role": "user", "content": prompt},
    ],
    response_format={"type": "json_object"},
)

# Step 1: Raw output จาก AI (ยังเป็น string)
raw_output = response.choices[0].message.content
print("=== Raw AI Output ===")
print(raw_output)
