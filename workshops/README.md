# Workshops

โฟลเดอร์นี้รวม Lab สำหรับการอบรม โดยแยกเนื้อหา Workshop ออกจากเอกสาร Lecture ในโฟลเดอร์ `docs/`

## Workshop List

| Lab | Folder | Goal |
|---|---|---|
| 1 | `lab-01-first-api-call` | เรียก AI Model ผ่าน Microsoft Foundry ครั้งแรก |
| 2 | `lab-02-prompt-to-json` | เขียน Prompt ให้ได้ JSON output |
| 3 | `lab-03-supplier-issue-analyzer` | สร้าง Mini AI Agent วิเคราะห์ Supplier Issue |
| 4 | `lab-04-it-ticket-classifier` | สร้าง Mini AI Agent แยกประเภท IT Ticket |
| 5 | `lab-05-mini-challenge` | ออกแบบ Use Case และ Prompt ของตนเอง |

## Bonus Labs (ถ้าเหลือเวลา หรือกลับไปทำต่อที่บ้าน)

| Lab | Folder | Goal |
|---|---|---|
| 6 | `lab-06-multi-turn-chatbot` | สร้าง Chatbot ที่จำบทสนทนาก่อนหน้าได้ (Multi-turn & Memory) |
| 7 | `lab-07-function-calling` | ให้ AI เรียกฟังก์ชัน Python เพื่อดึงข้อมูลจาก mock database (Function Calling) |

> ดูเนื้อหาประกอบใน `docs/07-prompt-engineering-advanced.md`, `docs/08-multi-turn-conversation.md`, `docs/09-function-calling.md`

## Before Running Labs

1. ติดตั้ง package

```bash
pip install -r requirements.txt
```

2. สร้างไฟล์ `.env` จาก `.env.example`
3. ใส่ API Key, Endpoint, Deployment และ API Version ที่ได้รับจากผู้สอน
4. รันไฟล์ `starter.py` ในแต่ละ Lab
