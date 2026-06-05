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

ticket = "User แจ้งว่าเข้าใช้งานระบบ ERP ไม่ได้หลังจากเปลี่ยนรหัสผ่านเมื่อเช้า"

prompt = f"""
You are an IT helpdesk triage assistant.

Analyze the IT ticket below.

Rules:
- Classify category as Network, Hardware, Software, Account/Login, ERP/System, Security, or Other.
- Set priority as Low, Medium, or High.
- Suggest the assigned team.
- Draft a short first response to the user in Thai.

Return JSON only with these fields:
summary, category, priority, assigned_team, first_response

Ticket:
{ticket}
"""

response = client.chat.completions.create(
    model=deployment_name,
    messages=[
        {"role": "system", "content": "You are an IT helpdesk AI assistant. Return JSON only."},
        {"role": "user", "content": prompt},
    ],
)

print(response.choices[0].message.content)
