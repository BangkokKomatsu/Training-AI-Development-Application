# AI Application Development: Build Your First Mini AI Agent with Microsoft Foundry

![AI Application Development Course](ChatGPT%20Image%20Jun%204%2C%202026%2C%2002_48_11%20PM.png)

คู่มือประกอบการอบรมสำหรับหลักสูตร **AI Application Development** ของ BKC  
เน้นการเรียนรู้การใช้งาน **Microsoft Foundry**, **API Key**, **Endpoint**, **Token**, **Prompt**, และการเขียนโปรแกรมด้วย **VS Code + Python** เพื่อสร้าง Mini AI Agent Prototype แบบง่าย

> เป้าหมายของ repository นี้คือแยกเนื้อหาเรียนกับ Workshop ให้ชัดเจน ผู้เรียนสามารถอ่านพื้นฐานก่อนลงมือทำ Lab และสามารถนำตัวอย่างไปปรับใช้หลังจบคอร์สได้

---

## Course Information

- **Course Name:** AI Application Development: Build Your First Mini AI Agent with Microsoft Foundry
- **Duration:** 1 day, 10:00 - 16:00
- **Format:** Lecture + Demo + Hands-on Workshop
- **Main Tools:** Microsoft Foundry, VS Code, Python
- **Output:** Mini AI Agent Prototype ที่เรียก AI Model ผ่าน API ได้

---

## Repository Structure

```text
.
├── README.md
├── COURSE_OUTLINE.md
├── requirements.txt
├── .env.example
├── .gitignore
├── agenda/
│   └── agenda-10-16.md
├── slides/
│   └── course-slides.md
├── docs/
│   ├── 00-overview.md
│   ├── 01-foundry-concept.md
│   ├── 02-api-key-endpoint.md
│   ├── 03-token-basics.md
│   ├── 04-prompt-engineering.md
│   ├── 05-vscode-python-setup.md
│   ├── 06-security-checklist.md
│   ├── 07-prompt-engineering-advanced.md
│   ├── 08-multi-turn-conversation.md
│   └── 09-function-calling.md
├── sample-data/
│   ├── supplier_issues.json
│   └── it_tickets.json
└── workshops/
    ├── README.md
    ├── lab-01-first-api-call/
    ├── lab-02-prompt-to-json/
    ├── lab-03-supplier-issue-analyzer/
    ├── lab-04-it-ticket-classifier/
    ├── lab-05-mini-challenge/
    ├── lab-06-multi-turn-chatbot/      (Bonus)
    └── lab-07-function-calling/        (Bonus)
```

---

## How to Use This Guide

### สำหรับผู้เรียน

1. อ่าน `docs/00-overview.md` เพื่อเข้าใจภาพรวม
2. ทำตาม `docs/05-vscode-python-setup.md` เพื่อติดตั้งเครื่องมือ
3. Copy `.env.example` เป็น `.env`
4. ใส่ API Key, Endpoint และ Deployment Name ที่ผู้สอนเตรียมให้
5. ทำ Lab ตามลำดับในโฟลเดอร์ `workshops/`

### สำหรับผู้สอน

1. เตรียม Microsoft Foundry project, deployment, endpoint และ API key สำหรับ workshop
2. กำหนด quota / rate limit ให้เหมาะสมกับจำนวนผู้เรียน
3. เตรียม `.env` ตัวอย่าง แต่ห้าม commit key จริง
4. ทดสอบ Lab ทั้งหมดก่อนวันอบรม
5. หลังอบรมควร rotate หรือ revoke key ที่ใช้ในห้องเรียน
6. ใช้ `slides/course-slides.md` สำหรับนำเสนอ (เปิดด้วย VS Code extension "Marp for VS Code" หรือ export เป็น PDF/PPTX)

---

## Workshop Overview

| Lab | Topic | Output |
|---|---|---|
| Lab 1 | First API Call | เรียก AI Model ผ่าน API สำเร็จครั้งแรก |
| Lab 2 | Prompt to JSON | ให้ AI ตอบเป็น JSON ที่นำไปใช้ต่อได้ |
| Lab 3 | Supplier Issue Analyzer | Mini AI Agent วิเคราะห์ปัญหา Supplier |
| Lab 4 | IT Ticket Classifier | Mini AI Agent แยกประเภท IT Ticket |
| Lab 5 | Mini Challenge | ผู้เรียนออกแบบ Use Case ของตัวเอง |
| Lab 6 (Bonus) | Multi-turn Chatbot | Chatbot ที่จำบทสนทนาก่อนหน้าได้ |
| Lab 7 (Bonus) | Function Calling | AI เรียกฟังก์ชัน Python เพื่อดึงข้อมูลจาก mock database |

---

## Important Security Notes

- ห้าม commit ไฟล์ `.env` ขึ้น GitHub
- ห้ามใส่ API Key ลงใน source code โดยตรง
- ห้ามแชร์ API Key ผ่าน Line, Email, Slide หรือเอกสารสาธารณะ
- ใช้ข้อมูลตัวอย่างเท่านั้น ห้ามใช้ข้อมูล Confidential, Customer Data, Contract, ราคา หรือ Personal Data จริงใน workshop
- ผลลัพธ์จาก AI ต้องมี Human Review ก่อนใช้งานจริง

---

## After This Course

หลังจบคอร์สนี้ ผู้เรียนจะสามารถสร้าง **Mini AI Agent Prototype** ได้ด้วยตนเอง โดยยังไม่ลงลึกเรื่อง RAG หรือ Agent แบบ Low-code ซึ่งจะต่อยอดในคอร์สถัดไป
