import json
import os
from datetime import datetime
from dotenv import load_dotenv
from openai import AzureOpenAI

load_dotenv()

client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
)

deployment_name = os.getenv("AZURE_OPENAI_DEPLOYMENT")

TEAM_ROUTING = {
    "Network": "Network Operations (NOC)",
    "Hardware": "Desktop Support",
    "Software": "Application Support",
    "Account/Login": "IT Helpdesk L1",
    "ERP/System": "ERP Support Team",
    "Security": "IT Security",
    "Other": "IT Helpdesk L1",
}


def classify_ticket(ticket_id: str, ticket: str) -> dict:
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
    result = json.loads(response.choices[0].message.content)
    result["ticket_id"] = ticket_id
    result["logged_at"] = datetime.now().strftime("%Y-%m-%d %H:%M")
    return result


# Load tickets from sample data
with open("sample-data/it_tickets.json", encoding="utf-8") as f:
    tickets = json.load(f)

all_results = []

for t in tickets:
    print(f"\n{'='*50}")
    print(f"Processing {t['ticket_id']}...")
    print(f"Input: {t['ticket']}")

    result = classify_ticket(t["ticket_id"], t["ticket"])
    all_results.append(result)

    routed_team = TEAM_ROUTING.get(result["category"], "IT Helpdesk L1")

    print(f"\n  Category      : {result['category']}")
    print(f"  Priority      : {result['priority']}")
    print(f"  Summary       : {result['summary']}")
    print(f"  Assigned Team : {result['assigned_team']}")
    print(f"\n  Routing --> {routed_team}")
    print(f"\n  --- First Response to User ---")
    print(result.get("first_response", ""))
    print(f"  ------------------------------")

# Save ticket log (สมมุติบันทึกลง ticketing system)
log_path = "ticket_log.json"
with open(log_path, "w", encoding="utf-8") as f:
    json.dump(all_results, f, ensure_ascii=False, indent=2)

# Routing Summary Table
print(f"\n{'='*50}")
print("=== Ticket Routing Summary ===")
print(f"{'Ticket':<10} {'Priority':<10} {'Category':<18} {'Routed To'}")
print(f"{'-'*65}")
for r in all_results:
    team = TEAM_ROUTING.get(r["category"], "IT Helpdesk L1")
    print(f"{r['ticket_id']:<10} {r['priority']:<10} {r['category']:<18} {team}")

print(f"\nTicket log saved to {log_path}")
