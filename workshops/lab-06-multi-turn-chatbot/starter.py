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

messages = [
    {"role": "system", "content": "คุณเป็นผู้ช่วยประจำโรงงานของ BKC ที่คอยช่วยเหลือผู้ใช้งาน ตอบให้กระชับ"}
]

print("Chatbot พร้อมแล้ว พิมพ์ 'exit' หรือ 'quit' เพื่อจบโปรแกรม\n")

while True:
    user_input = input("You: ")
    if user_input.lower() in ("exit", "quit"):
        break

    # append ข้อความของ user เข้า messages ด้วย role "user"
    messages.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model=deployment_name,
        messages=messages,
    )

    assistant_reply = response.choices[0].message.content
    print(f"AI: {assistant_reply}\n")

    # append คำตอบของ AI เข้า messages ด้วย role "assistant"
    # เพื่อให้รอบถัดไป AI ยังจำบทสนทนานี้ได้
    messages.append({"role": "assistant", "content": assistant_reply})
