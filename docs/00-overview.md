# 00 - Course Overview

## เป้าหมายของคอร์ส

คอร์สนี้พาผู้เรียนเข้าใจการสร้าง AI Application เบื้องต้น โดยใช้ Microsoft Foundry ที่ BKC เตรียมไว้ให้ และเขียน Python ผ่าน VS Code เพื่อเรียกใช้งาน AI Model ผ่าน API

หลังจบคอร์ส ผู้เรียนควรสามารถสร้าง Mini AI Agent Prototype แบบง่ายได้ เช่น

- Factory Issue Analyzer (Lab 3) — วิเคราะห์และจัดหมวดหมู่ปัญหาจาก Supplier/หน้างานอัตโนมัติ
- Factory Issue Batch Excel (Lab 4) — อ่าน Excel ทีละหลายแถวแล้วให้ AI สรุปผลลง Excel กลับ
- Mini Challenge (Lab 5) — ต่อยอด use case ของตัวเองจากโครงสร้างที่เรียนมา มีตัวอย่างอ้างอิงคือ Document Completeness Checker (เช็คว่าเอกสารจาก Supplier ครบถ้วนหรือไม่)
- Multi-turn Chatbot และ Function Calling (Lab 6-7, บทเรียนเสริม) — สำหรับผู้ที่อยากต่อยอดเป็น Agent ที่โต้ตอบหลายรอบหรือเรียกใช้ฟังก์ชันเอง

---

## แนวคิดหลัก

```text
User Input
    ↓
Prompt
    ↓
Python Application
    ↓
Microsoft Foundry Endpoint + API Key
    ↓
AI Model
    ↓
Response
    ↓
Text / JSON / Email Draft / Action Plan
```

---

## สิ่งที่ไม่ใช่เป้าหมายของคอร์สนี้

- ยังไม่ใช่ RAG Chatbot เต็มรูปแบบ
- ยังไม่ใช่ M365 Low-code Agent
- ยังไม่เชื่อมต่อ Production System จริง
- ยังไม่ให้ AI ทำงานอัตโนมัติหลายขั้นตอนโดยไม่มีคนตรวจ

คอร์สนี้เป็นพื้นฐานเพื่อให้ผู้เรียนเข้าใจ API, Prompt, Token และ Mini AI Agent ก่อนต่อยอดไปคอร์สถัดไป
