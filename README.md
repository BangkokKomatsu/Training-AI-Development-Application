# AI Application Development: Build Your First Mini AI Agent with Microsoft Foundry

![AI Application Development Course](ChatGPT%20Image%20Jun%204%2C%202026%2C%2002_48_11%20PM.png)

คู่มือประกอบการอบรมสำหรับหลักสูตร **AI Application Development** ของ BKC  
เน้นการเรียนรู้การใช้งาน **Microsoft Foundry**, **API Key**, **Endpoint**, **Token**, **Prompt**, และการเขียนโปรแกรมด้วย **VS Code + Python** เพื่อสร้าง Mini AI Agent Prototype แบบง่าย

> เป้าหมายของ repository นี้คือแยกเนื้อหาเรียนกับ Workshop ให้ชัดเจน ผู้เรียนสามารถอ่านพื้นฐานก่อนลงมือทำ Lab และสามารถนำตัวอย่างไปปรับใช้หลังจบคอร์สได้

---

## Course Information

- **Course Name:** AI Application Development: Build Your First Mini AI Agent with Microsoft Foundry
- **ชื่อภาษาไทย:** พัฒนา AI Application เบื้องต้น: สร้าง Mini AI Agent ด้วย Microsoft Foundry, API Key, Token และ Prompt
- **Duration:** 1 day, 10:00 - 16:00
- **Format:** Lecture + Demo + Hands-on Workshop
- **Main Tools:** Microsoft Foundry, VS Code, Python, Streamlit
- **Output:** Mini AI Agent Prototype ที่เรียก AI Model ผ่าน API ได้

---

## เหมาะกับใคร

- พนักงานภายใน BKC เช่น ฝ่ายผลิต, ซ่อมบำรุง, QA, ความปลอดภัย, คลังสินค้า, IT, หรือ Supplier Coordinator
- ผู้ที่เคยใช้งาน ChatGPT / Copilot / Gemini ผ่านหน้าเว็บ และต้องการเข้าใจการใช้งานผ่าน API
- ผู้ที่ต้องการเข้าใจการสร้าง Mini AI Agent Prototype และหน้าเว็บแอปพลิเคชันอย่างง่าย ก่อนต่อยอดไป RAG Chatbot หรือ M365 AI Agent

### พื้นฐานผู้เข้าอบรม

- ใช้งานคอมพิวเตอร์และอินเทอร์เน็ตได้คล่อง
- เข้าใจการใช้งานไฟล์และโฟลเดอร์บน Windows
- มีพื้นฐานการใช้งาน VS Code หรือพร้อมเรียนรู้ในวันอบรม
- เคยเห็น Python เบื้องต้นจะช่วยให้เรียนได้เร็วขึ้น แต่ไม่จำเป็นต้องเป็น programmer เต็มตัว
- อ่านตัวอย่างภาษาอังกฤษพื้นฐานใน Prompt และ Response ได้บ้าง

---

## สิ่งที่จะได้เรียนรู้

- AI Application และ Mini AI Agent คืออะไร
- Microsoft Foundry เกี่ยวข้องกับ AI API อย่างไร
- ความหมายของ Endpoint, API Key, Deployment Name และ Model
- Token คืออะไร และมีผลต่อค่าใช้จ่าย/ข้อจำกัดอย่างไร
- วิธีเก็บ API Key อย่างปลอดภัยด้วย `.env`
- วิธีตั้งค่า VS Code + Python สำหรับเรียก AI API
- วิธีเขียน Prompt แบบ Role, Task, Context, Rules, Output Format และ Input
- เทคนิค Few-Shot Prompting การใส่ตัวอย่างข้อความเพื่อให้ AI เข้าใจบริบทศัพท์เทคนิคในโรงงานมากขึ้น
- วิธีการตั้งค่าพารามิเตอร์โมเดล (Temperature & Max Tokens) เพื่อควบคุมความแม่นยำและความคิดสร้างสรรค์
- วิธีให้ AI ตอบกลับเป็น JSON อย่างแม่นยำ
- วิธีเขียนโค้ดรองรับข้อผิดพลาด (Error Handling & API Resilience) เพื่อไม่ให้สคริปต์หยุดทำงานเมื่อเน็ตหลุดหรือข้อมูลผิดพลาด
- วิธีสร้างหน้าเว็บแอปอย่างง่ายด้วย Streamlit พร้อมการออกแบบแบบ Human-in-the-Loop เพื่อให้พนักงานมีโอกาสตรวจสอบผลลัพธ์จาก AI ก่อนกดยืนยันใช้งานจริง
- วิธีอ่านข้อมูลและเขียนผลวิเคราะห์กลับลงไฟล์ Excel (Pandas + Openpyxl) สำหรับประมวลผลเป็นกลุ่ม (Batch)

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
│   └── factory_issues.json
└── workshops/
    ├── README.md
    ├── lab-01-first-api-call/
    ├── lab-02-prompt-to-json/
    ├── lab-03-factory-issue-analyzer/
    ├── lab-04-factory-issue-batch-excel/
    ├── lab-05-mini-challenge/
    ├── lab-06-multi-turn-chatbot/      (Bonus)
    └── lab-07-function-calling/        (Bonus)
```

---

## How to Use This Guide

### ผู้เข้าอบรมต้องเตรียม

- Notebook ส่วนตัว พร้อม internet
- ติดตั้ง VS Code
- ติดตั้ง Python 3.10 ขึ้นไป
- ติดตั้ง Git หากต้องการ clone repository
- ได้รับ API Key, Endpoint และ Deployment Name จากผู้สอนหรือ BKC ก่อนเริ่ม workshop
- ข้อมูลตัวอย่างที่ไม่ใช่ข้อมูลจริงหรือข้อมูลลับ

> หมายเหตุ: ห้ามใช้ข้อมูล Confidential, Customer Data, Contract, ราคา, Personal Data หรือ API Key ส่วนตัวใน workshop

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
| Lab 3 | Factory Issue Analyzer | Mini AI Agent วิเคราะห์ปัญหาโรงงาน (Streamlit UI) |
| Lab 4 | Factory Issue Batch Excel | ประมวลผลลูปคัดแยกปัญหาอัตโนมัติ (Pandas) |
| Lab 5 | Mini Challenge | ผู้เรียนออกแบบ Use Case ของตัวเอง |
| Lab 6 (Bonus) | Multi-turn Chatbot | Chatbot ที่จำบทสนทนาก่อนหน้าได้ |
| Lab 7 (Bonus) | Function Calling | AI เรียกฟังก์ชัน Python เพื่อดึงข้อมูลสถานะเครื่องจักรจำลอง |

---

## Agenda เบื้องต้น เวลา 10:00 - 16:00

| เวลา | หัวข้อ | รูปแบบ | รายละเอียด |
|---|---|---|---|
| 10:00 - 10:20 | Introduction & Course Objective | Lecture | แนะนำเป้าหมายหลักสูตร ภาพรวม Mini AI Agent และหน้าเว็บแอปที่จะได้สร้าง |
| 10:20 - 10:50 | AI Application, Microsoft Foundry & API Concept | Lecture + Demo | อธิบาย Foundry, Endpoint, Deployment, API Key, Request และ Response |
| 10:50 - 11:15 | API Key Security & Token Basics | Lecture | วิธีเก็บ Key, ความหมายของ Token, การประมาณการค่าใช้จ่าย (Cost) และ Rate Limits |
| 11:15 - 12:00 | VS Code + Python Setup & Prompt Basics | Hands-on | ตั้งค่า project, การปรับพารามิเตอร์ (Temperature) และเขียน Prompt แบบ Few-Shot |
| 12:00 - 13:00 | Lunch Break | - | - |
| 13:00 - 13:30 | Workshop 1: First API Call | Hands-on Lab | เรียก AI Model ผ่าน Microsoft Foundry ด้วย Python |
| 13:30 - 14:00 | Workshop 2: Structured Output & JSON | Hands-on Lab | ให้ AI ตอบกลับเป็น JSON เพื่อนำไปใช้ต่อในโค้ด |
| 14:00 - 14:45 | Workshop 3: Factory Issue & Streamlit UI | Hands-on Lab | วิเคราะห์ปัญหาโรงงาน สร้างเว็บแอป และออกแบบ Human-in-the-loop |
| 14:45 - 15:00 | Break | - | - |
| 15:00 - 15:30 | Workshop 4: Excel Batch & Error Handling | Hands-on Lab | วนลูปคัดแยกข้อมูล Excel จำนวนมาก พร้อมเขียน `try-except` ป้องกันโปรแกรมพัง |
| 15:30 - 15:50 | Mini Challenge: Design Your Own Use Case | Activity | ผู้เรียนออกแบบ Prompt และต่อยอด UI บนหน้าเว็บ Streamlit ของตนเอง |
| 15:50 - 16:00 | Wrap-up, Security Checklist & Next Step | Summary | สรุปสิ่งที่เรียนและแนวทางต่อยอด |

> ตารางเวลาแบบละเอียด (รวม breakdown ต่อบล็อก): [`agenda/agenda-10-16.md`](agenda/agenda-10-16.md)

---

## ขอบเขตของคอร์สนี้

| ครอบคลุมในคอร์สนี้ | ยังไม่ลงลึกในคอร์สนี้ |
|---|---|
| API Key, Endpoint, Token และ Prompt | RAG Chatbot จากเอกสารจำนวนมาก |
| การเรียก AI API ด้วย Python | Agent เต็มรูปแบบที่เชื่อมหลายระบบ |
| การรับ Response เป็น Text / JSON | Production-grade deployment |
| หน้าเว็บแอปพลิเคชันอย่างง่าย (Streamlit) | Governance ระดับองค์กรแบบเต็มรูปแบบ |
| การเขียนผลลัพธ์เป็นตาราง Excel | การเชื่อมต่อฐานข้อมูลจริง |
| Security เบื้องต้นสำหรับ API Key | |

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
