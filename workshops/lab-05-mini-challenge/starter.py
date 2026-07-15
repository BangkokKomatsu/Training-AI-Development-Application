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


def analyze_custom_usecase(user_input: str) -> dict:
    prompt = f"""
    [TODO: กำหนด Role ของ AI ที่นี่ เช่น "คุณเป็นผู้ช่วย AI สำหรับฝ่าย..."]

    วิเคราะห์ข้อความต่อไปนี้

    Rules:
    - [TODO: เพิ่มกฎข้อที่ 1]
    - [TODO: เพิ่มกฎข้อที่ 2]

    ตอบกลับเป็น JSON เท่านั้น โดยมี field ดังนี้:
    - [TODO: ชื่อ field ที่ 1]
    - [TODO: ชื่อ field ที่ 2]

    ข้อความนำเข้า:
    {user_input}
    """
    response = client.chat.completions.create(
        model=deployment_name,
        messages=[
            {"role": "system", "content": "คุณเป็นผู้ช่วย AI ที่คอยช่วยเหลือผู้ใช้งาน ตอบกลับเป็น JSON เท่านั้น"},
            {"role": "user", "content": prompt},
        ],
        response_format={"type": "json_object"},
    )
    return json.loads(response.choices[0].message.content)


# ลองใส่ข้อความตัวอย่างของ Use Case ที่คุณเลือก (ดู README.md หัวข้อ "Choose One Use Case")
sample_input = "[TODO: ใส่ข้อความตัวอย่างที่ต้องการให้ AI วิเคราะห์ที่นี่]"

result = analyze_custom_usecase(sample_input)

print("=== ผลลัพธ์จาก AI ===")
for key, value in result.items():
    print(f"{key}: {value}")
