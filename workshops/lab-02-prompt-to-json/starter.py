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

print(response.choices[0].message.content)
