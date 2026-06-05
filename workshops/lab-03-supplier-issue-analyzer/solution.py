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

result = response.choices[0].message.content
print(result)
