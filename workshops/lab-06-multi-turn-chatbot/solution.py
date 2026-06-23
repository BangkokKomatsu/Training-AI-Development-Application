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

SYSTEM_PROMPT = {
    "role": "system",
    "content": "You are a helpful factory assistant at BKC. Keep answers short.",
}

# จำกัดจำนวนข้อความ (ไม่รวม system) ที่จะส่งกลับไปใน history เพื่อคุม token
MAX_HISTORY_MESSAGES = 6

messages = [SYSTEM_PROMPT]

print("Chatbot พร้อมแล้ว พิมพ์ 'exit' หรือ 'quit' เพื่อจบโปรแกรม\n")

while True:
    user_input = input("You: ")
    if user_input.lower() in ("exit", "quit"):
        break

    messages.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model=deployment_name,
        messages=messages,
    )

    assistant_reply = response.choices[0].message.content
    print(f"AI: {assistant_reply}")

    messages.append({"role": "assistant", "content": assistant_reply})

    # ตัด history เก่าออกถ้ายาวเกินกำหนด (เก็บ system ไว้เสมอ)
    history = messages[1:]
    if len(history) > MAX_HISTORY_MESSAGES:
        history = history[-MAX_HISTORY_MESSAGES:]
        messages = [SYSTEM_PROMPT] + history

    print(f"[messages ในระบบตอนนี้: {len(messages)} ข้อความ]\n")
