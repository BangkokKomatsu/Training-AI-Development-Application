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

use_case_name = "Document Completeness Checker"

input_text = "Supplier ส่ง invoice มาแต่ไม่มี PO number และไม่มี delivery date"

prompt = f"""
You are an AI assistant for document checking.

Use case: {use_case_name}

Analyze the input below.

Rules:
- Do not assume missing fields.
- Identify missing information.
- Explain the business risk.
- Draft a polite reply message in Thai.

Return JSON only with these fields:
document_status, missing_fields, risk, reply_message

Input:
{input_text}
"""

response = client.chat.completions.create(
    model=deployment_name,
    messages=[
        {"role": "system", "content": "You are a business AI assistant. Return JSON only."},
        {"role": "user", "content": prompt},
    ],
    response_format={"type": "json_object"},
)

# แปลง JSON string เป็น dict แล้วแสดงผลทีละ field แทนการ print ดิบทั้งก้อน
result = json.loads(response.choices[0].message.content)

print("=" * 50)
print(f"       {use_case_name}")
print("=" * 50)
print(f"  Status         : {result.get('document_status')}")
print(f"  Missing Fields : {result.get('missing_fields')}")
print(f"  Risk           : {result.get('risk')}")
print(f"  Reply Message  :\n{result.get('reply_message')}")
print("=" * 50)
