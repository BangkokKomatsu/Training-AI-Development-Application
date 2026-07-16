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

# ต่างจาก starter.py ตรงนี้: user_input มาจากคนพิมพ์เอง ไม่ใช่ข้อความตายตัว
user_input = input("คุณต้องการถามอะไร? > ")

response = client.chat.completions.create(
    model=deployment_name,
    messages=[
        {"role": "system", "content": "คุณเป็นผู้ช่วย AI ที่คอยช่วยเหลือผู้ใช้งาน"},
        {"role": "user", "content": user_input},
    ],

)

print("คำตอบของ AI:", response.choices[0].message.content)
