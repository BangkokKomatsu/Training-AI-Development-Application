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
# 💡 ลองเปลี่ยนเป็นรับ input จาก user:
# issue_report = input("กรุณากรอก Issue Report: ")

prompt = f"""
คุณเป็นผู้ช่วย AI สำหรับจัดการปัญหา Supplier ของ BKC

วิเคราะห์รายงานปัญหาด้านล่างนี้

Rules:
- ห้ามเดาข้อมูลที่ขาดหายไป
- ถ้าข้อมูลขาดหายไป ให้ระบุให้ชัดเจน
- จัดหมวดหมู่ปัญหาเป็น Quality, Delivery, Document, IT, Commercial หรือ Other
- กำหนดความเร่งด่วน (priority) เป็น Low, Medium หรือ High
- เขียนค่าของ "summary" และ "recommended_action" เป็นภาษาไทย เพื่อให้ทีมหน้างาน
  อ่านผลลัพธ์ได้ทันทีโดยไม่ต้องแปลเอง

ตอบกลับเป็น JSON เท่านั้น โดยมี field ดังนี้:
summary, category, priority, missing_information, recommended_action

รายงานปัญหา:
{issue_report}
"""

# response_format={"type": "json_object"} บังคับให้ AI ตอบกลับเป็น JSON string ล้วน ๆ
response = client.chat.completions.create(
    model=deployment_name,
    messages=[
        {"role": "system", "content": "คุณตอบกลับเป็น JSON ที่ถูกต้องและกระชับเท่านั้น"},
        {"role": "user", "content": prompt},
    ],
    response_format={"type": "json_object"},
)

# Step 1: Parse JSON จาก AI — content ตอนนี้เป็น string เฉย ๆ ต้องแปลงเป็น dict ก่อนใช้งาน
result = json.loads(response.choices[0].message.content)

# Step 2: แสดง field แต่ละตัวแบบอ่านง่าย
print()
print("=" * 50)
print("       AI Analysis Result")
print("=" * 50)
print(f"  📋 Summary  : {result['summary']}")
print(f"  🏷️  Category : {result['category']}")
print(f"  🚨 Priority  : {result['priority']}")
print(f"  ❓ Missing   : {result.get('missing_information', '-')}")
print(f"  ✅ Action    : {result['recommended_action']}")
print("=" * 50)

# Step 3: ใช้ priority field ตัดสินใจทำสิ่งต่อไป
print()
print("=" * 50)
print("       Routing Decision")
print("=" * 50)
if result["priority"] == "High":
    print("  🔴 HIGH PRIORITY — แจ้ง Procurement Manager ทันที")
elif result["priority"] == "Medium":
    print("  🟡 MEDIUM — สร้าง Ticket ใน ERP ติดตามใน 24 ชั่วโมง")
else:
    print("  🟢 LOW — บันทึกไว้ติดตามตาม SLA ปกติ")
print("=" * 50)

# Step 4: บันทึก JSON ลงไฟล์ (สมมุติว่าส่งต่อระบบอื่น เช่น ERP, dashboard)
with open("lab02_output.json", "w", encoding="utf-8") as f:
    json.dump(result, f, ensure_ascii=False, indent=2)

print()
print("💾 Saved to lab02_output.json — พร้อมส่งต่อระบบอื่น")
