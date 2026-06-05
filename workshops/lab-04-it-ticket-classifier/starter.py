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

# Step 1: Parse JSON
result = json.loads(response.choices[0].message.content)

# Step 2: แสดง field แต่ละตัว
print("=== IT Ticket Classification ===")
print(f"Category      : {result['category']}")
print(f"Priority      : {result['priority']}")
print(f"Summary       : {result['summary']}")
print(f"Assigned Team : {result['assigned_team']}")

# Step 3: แสดง first_response ที่พร้อมส่งกลับ user
print("\n=== First Response to User ===")
print(result.get("first_response", ""))

# TODO: ลองเพิ่ม routing ตาม category
# TEAM_ROUTING = {
#     "Account/Login": "IT Helpdesk L1",
#     "ERP/System": "ERP Support Team",
#     "Network": "Network Operations (NOC)",
# }
# team = TEAM_ROUTING.get(result["category"], "IT Helpdesk L1")
# print(f"Route to: {team}")

# TODO: ลองบันทึก ticket log ลงไฟล์
# with open("ticket_log.json", "w", encoding="utf-8") as f:
#     json.dump(result, f, ensure_ascii=False, indent=2)
