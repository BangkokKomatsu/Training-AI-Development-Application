# โหลดค่า config (API Key, Endpoint, ...) จากไฟล์ .env แทนการ hardcode ในโค้ด
import os
from dotenv import load_dotenv
from openai import AzureOpenAI

load_dotenv()

# client คือ "สายโทรศัพท์" ที่โปรแกรมใช้คุยกับ Microsoft Foundry
client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
)

deployment_name = os.getenv("AZURE_OPENAI_DEPLOYMENT")

response = client.chat.completions.create(
    model=deployment_name,
    # messages คือบทสนทนาที่ส่งให้ AI:
    #   - role "system"  = กำหนดบุคลิก/หน้าที่ของ AI (ผู้เรียนไม่เห็นข้อความนี้)
    #   - role "user"    = คำถาม/คำสั่งจากผู้ใช้งานจริง
    messages=[
        {"role": "system", "content": "You are a helpful AI assistant."},
        {"role": "user", "content": "Explain what an API key is in simple Thai language."},
    ],
)

print(response.choices[0].message.content)
