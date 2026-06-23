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

# Mock database (สมมุติว่าเป็นข้อมูลเซ็นเซอร์เครื่องจักร)
MACHINE_DB = {
    "MAC-001": {"status": "Overheating", "temperature_celsius": 85},
    "MAC-002": {"status": "Normal", "temperature_celsius": 45},
    "MAC-003": {"status": "Offline", "temperature_celsius": 0},
}


def get_machine_status(machine_id: str) -> dict:
    return MACHINE_DB.get(machine_id, {"status": "Unknown", "temperature_celsius": "-"})


# TODO 1: เพิ่ม description และ parameter ให้ AI เข้าใจว่าฟังก์ชันนี้ใช้ทำอะไร
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_machine_status",
            "description": "Get the current status and temperature of a machine by machine_id",
            "parameters": {
                "type": "object",
                "properties": {
                    "machine_id": {
                        "type": "string",
                        "description": "Machine ID, e.g. MAC-001",
                    }
                },
                "required": ["machine_id"],
            },
        },
    }
]

messages = [
    {"role": "system", "content": "You are a helpful factory assistant at BKC."},
    {"role": "user", "content": "สถานะของเครื่อง MAC-001 ตอนนี้เป็นอย่างไร อุณหภูมิเท่าไหร่"},
]

response = client.chat.completions.create(
    model=deployment_name,
    messages=messages,
    tools=tools,
)

message = response.choices[0].message

if message.tool_calls:
    for tool_call in message.tool_calls:
        if tool_call.function.name == "get_machine_status":
            args = json.loads(tool_call.function.arguments)
            print(f"[AI ขอเรียกฟังก์ชัน get_machine_status กับ machine_id={args['machine_id']}]")

            # TODO 2: เรียกฟังก์ชันจริงด้วย argument ที่ AI ส่งมา
            result = get_machine_status(args["machine_id"])
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
