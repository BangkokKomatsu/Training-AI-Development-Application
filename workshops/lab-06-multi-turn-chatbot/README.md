# Lab 6 (Bonus) - Multi-turn Chatbot with Memory

## Goal

สร้าง chatbot บน command line ที่ "จำ" บทสนทนาก่อนหน้าได้ โดยใช้แนวคิดจาก `docs/08-multi-turn-conversation.md`

## What You Will Learn

- โครงสร้าง `messages` แบบ list และความหมายของ role: `system`, `user`, `assistant`
- การ append ข้อความเข้า history แล้วส่งกลับไปทั้งหมดในรอบถัดไป
- ผลกระทบของ conversation history ต่อจำนวน token ที่ใช้

## Conversation Flow

```text
messages = [system]
   |
   +-- user พิมพ์คำถาม 1 --> append user_1 --> call API --> append assistant_1
   |
   +-- user พิมพ์คำถาม 2 --> append user_2 --> call API (เห็น user_1, assistant_1 ด้วย) --> append assistant_2
   |
   ... ทำซ้ำจนพิมพ์ "exit"
```

## Run

```bash
python workshops/lab-06-multi-turn-chatbot/starter.py
```

พิมพ์คุยกับ AI ได้หลายรอบ พิมพ์ `exit` หรือ `quit` เพื่อจบโปรแกรม

## Challenge

1. ถามคำถามต่อเนื่องที่ต้องอ้างอิงคำตอบก่อนหน้า เช่น ถามชื่อ AI assistant ในรอบแรก แล้วถามว่า "ชื่ออะไรนะ" ในรอบถัดไป
2. เพิ่มการ print จำนวนข้อความใน `messages` ทุกรอบ เพื่อดูว่า history โตขึ้นเรื่อย ๆ
3. (Advanced) ลองจำกัด history ให้เก็บแค่ 6 ข้อความล่าสุด (ไม่รวม system) เพื่อคุม token ไม่ให้บทสนทนายาวเกินไป — ดูตัวอย่างใน `solution.py`
