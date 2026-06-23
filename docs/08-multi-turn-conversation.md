# 08 - Multi-turn Conversation & Memory

> เนื้อหาเสริม (Bonus) — ใช้เวลาประมาณ 20-30 นาที เหมาะสำหรับกลุ่มที่ทำ Lab 1-4 เสร็จก่อนเวลา

---

## 1. ทำไม Lab 1-4 ถึง "ไม่มี Memory"

ใน Lab 1-4 ทุกครั้งที่เรียก `client.chat.completions.create()` เราส่ง `messages` ใหม่ทั้งหมด AI จึง**ไม่จำ**ว่าคุยอะไรไปก่อนหน้า แต่ละ request คือการคุยครั้งใหม่เสมอ

```python
messages=[
    {"role": "system", "content": "You are a helpful AI assistant."},
    {"role": "user", "content": "Explain what an API key is."},
]
```

---

## 2. หลักการของ Multi-turn Conversation

`messages` คือ **list ของบทสนทนาทั้งหมด** ตั้งแต่ต้นจนถึงปัจจุบัน ทุกครั้งที่ได้ response กลับมา ให้เก็บ (append) ทั้งคำถามและคำตอบเข้าไปใน list นี้ แล้วส่ง list ทั้งหมดไปใหม่ในรอบถัดไป

```text
Turn 1:
messages = [system, user_1]
   --> AI ตอบ assistant_1
   --> messages = [system, user_1, assistant_1]

Turn 2:
messages = [system, user_1, assistant_1, user_2]
   --> AI ตอบ assistant_2 (รู้ context จาก turn 1 ด้วย)
   --> messages = [system, user_1, assistant_1, user_2, assistant_2]
```

---

## 3. Role ทั้ง 3 ใน messages

| Role | ความหมาย |
|---|---|
| `system` | กำหนดบทบาทและกฎของ AI ตั้งแต่ต้น (ส่งครั้งเดียวพอ มักอยู่บนสุด) |
| `user` | ข้อความจากผู้ใช้ในแต่ละรอบ |
| `assistant` | คำตอบของ AI ในรอบก่อนหน้า ที่เราเก็บไว้แล้วส่งกลับไปเพื่อให้ AI "จำ" ได้ |

---

## 4. โค้ดตัวอย่าง (concept)

```python
messages = [
    {"role": "system", "content": "You are a helpful procurement assistant."}
]

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

    # เก็บคำตอบไว้ใน history เพื่อให้รอบถัดไป AI ยังจำได้
    messages.append({"role": "assistant", "content": assistant_reply})
```

---

## 5. ข้อควรระวัง

- ยิ่งคุยนาน `messages` ยิ่งยาว ➜ ใช้ **token ต่อ request เพิ่มขึ้นเรื่อย ๆ** (เกี่ยวกับ `docs/03-token-basics.md`)
- หากบทสนทนายาวเกินไป อาจต้องตัด history เก่าออก หรือสรุป (summarize) ประวัติเก่าเป็นข้อความสั้น ๆ แทน
- Memory นี้อยู่แค่ใน "ตัวแปรของโปรแกรม" ระหว่างที่โปรแกรมยังรันอยู่ ถ้าปิดโปรแกรม ประวัติจะหายไป (ยังไม่ใช่การบันทึกลง database)

---

## 6. ลองทำ (Try it during class)

ไปที่ `workshops/lab-06-multi-turn-chatbot/`:

1. รัน `starter.py` แล้วลองพิมพ์คุยกับ AI หลายรอบ สังเกตว่า AI จำสิ่งที่คุยก่อนหน้าได้หรือไม่
2. ลองถามคำถามที่ "อ้างอิงคำตอบก่อนหน้า" เช่น ถาม "สรุปสิ่งที่คุยมาให้หน่อย" ในรอบสุดท้าย
3. (Challenge) ลองเพิ่มการ print จำนวนข้อความใน `messages` ทุกรอบ เพื่อดูว่า history ยาวขึ้นเรื่อย ๆ อย่างไร
