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
    response_format={ "type": "json_object" } # บังคับให้ AI ตอบเป็น JSON เสมอ
)

# Step 1: Parse JSON
result = json.loads(response.choices[0].message.content)

# Step 2: แสดง field แต่ละตัว
print("=== Factory Issue Analysis ===")
print(f"Category  : {result.get('category')}")
print(f"Priority  : {result.get('priority')}")
print(f"Summary   : {result.get('summary')}")
print(f"Tools     : {result.get('tools_needed')}")
print(f"Action    : {result.get('recommended_action')}")

print("\n=== Safety Warning ===")
print(result.get("safety_warning", ""))

# TODO: ลองเขียนไฟล์ app_streamlit.py เพื่อทำหน้าเว็บ!
