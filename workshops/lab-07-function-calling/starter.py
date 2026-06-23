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

# Mock database (สมมุติว่าเป็นข้อมูลจากระบบ ERP)
SUPPLIER_DB = {
    "SUP-001": {"status": "Delayed", "eta": "2026-06-20"},
    "SUP-002": {"status": "On Time", "eta": "2026-06-15"},
    "SUP-003": {"status": "Pending Documents", "eta": "-"},
}


def get_supplier_status(supplier_id: str) -> dict:
    return SUPPLIER_DB.get(supplier_id, {"status": "Unknown", "eta": "-"})


# TODO 1: เพิ่ม description และ parameter ให้ AI เข้าใจว่าฟังก์ชันนี้ใช้ทำอะไร
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
    }
]

messages = [
    {"role": "system", "content": "You are a helpful procurement assistant at BKC."},
    {"role": "user", "content": "สถานะของ SUP-001 ตอนนี้เป็นอย่างไร และคาดว่าจะถึงเมื่อไหร่"},
]

response = client.chat.completions.create(
    model=deployment_name,
    messages=messages,
    tools=tools,
)

message = response.choices[0].message

if message.tool_calls:
    for tool_call in message.tool_calls:
        if tool_call.function.name == "get_supplier_status":
            args = json.loads(tool_call.function.arguments)
            print(f"[AI ขอเรียกฟังก์ชัน get_supplier_status กับ supplier_id={args['supplier_id']}]")

            # TODO 2: เรียกฟังก์ชันจริงด้วย argument ที่ AI ส่งมา
            result = get_supplier_status(args["supplier_id"])
            print(f"[ผลลัพธ์จากฟังก์ชัน: {result}]")

            # TODO 3: ส่ง message ของ AI (ที่มี tool_calls) และผลลัพธ์ฟังก์ชันกลับเข้า messages
            messages.append(message)
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
