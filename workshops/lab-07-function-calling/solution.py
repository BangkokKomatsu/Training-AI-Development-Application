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

SUPPLIER_DB = {
    "SUP-001": {"status": "Delayed", "eta": "2026-06-20"},
    "SUP-002": {"status": "On Time", "eta": "2026-06-15"},
    "SUP-003": {"status": "Pending Documents", "eta": "-"},
}

OPEN_TICKETS_DB = {
    "Procurement": 4,
    "IT Helpdesk": 12,
    "ERP Support": 2,
}


def get_supplier_status(supplier_id: str) -> dict:
    return SUPPLIER_DB.get(supplier_id, {"status": "Unknown", "eta": "-"})


def get_open_ticket_count(team: str) -> dict:
    return {"team": team, "open_tickets": OPEN_TICKETS_DB.get(team, 0)}


tools = [
    {
        "type": "function",
        "function": {
            "name": "get_supplier_status",
            "description": "Get the latest order status and ETA for a supplier by supplier_id",
            "parameters": {
                "type": "object",
                "properties": {
                    "supplier_id": {
                        "type": "string",
                        "description": "Supplier ID, e.g. SUP-001",
                    }
                },
                "required": ["supplier_id"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "get_open_ticket_count",
            "description": "Get the number of open tickets assigned to a team",
            "parameters": {
                "type": "object",
                "properties": {
                    "team": {
                        "type": "string",
                        "description": "Team name, e.g. Procurement, IT Helpdesk, ERP Support",
                    }
                },
                "required": ["team"],
            },
        },
    },
]

AVAILABLE_FUNCTIONS = {
    "get_supplier_status": get_supplier_status,
    "get_open_ticket_count": get_open_ticket_count,
}

messages = [
    {"role": "system", "content": "คุณเป็นผู้ช่วยฝ่ายจัดซื้อของ BKC ที่คอยช่วยเหลือผู้ใช้งาน"},
    {
        "role": "user",
        "content": "สถานะของ SUP-001 เป็นอย่างไร และตอนนี้ทีม Procurement มี ticket ที่ยังไม่ปิดกี่ใบ",
    },
]

response = client.chat.completions.create(
    model=deployment_name,
    messages=messages,
    tools=tools,
)

message = response.choices[0].message

if message.tool_calls:
    messages.append(message)

    for tool_call in message.tool_calls:
        function_name = tool_call.function.name
        args = json.loads(tool_call.function.arguments)
        print(f"[AI ขอเรียกฟังก์ชัน {function_name} ด้วย {args}]")

        function_to_call = AVAILABLE_FUNCTIONS[function_name]
        result = function_to_call(**args)
        print(f"[ผลลัพธ์: {result}]")

        messages.append(
            {
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": json.dumps(result),
            }
        )

    final_response = client.chat.completions.create(
        model=deployment_name,
        messages=messages,
    )
    print("\nAI:", final_response.choices[0].message.content)
else:
    print("\nAI:", message.content)
