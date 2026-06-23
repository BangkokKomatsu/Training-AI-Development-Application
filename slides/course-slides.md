---
marp: true
theme: default
paginate: true
size: 16:9
backgroundColor: #fff
---

<!-- _class: lead -->

# AI Application Development
## สร้าง Mini AI Agent ด้วย Microsoft Foundry

API Key • Endpoint • Token • Prompt • Python • Streamlit • Excel

**ระยะเวลา:** 1 วัน (10:00 - 16:00)
**รูปแบบ:** Lecture + Demo + Hands-on Workshop

---

## Agenda วันนี้

| เวลา | หัวข้อ | รูปแบบ |
|---|---|---|
| 10:00 - 10:20 | Introduction & Course Objective | Lecture |
| 10:20 - 10:50 | Microsoft Foundry & API Concept | Lecture + Demo |
| 10:50 - 11:15 | API Key Security & Token Cost Estimation | Lecture |
| 11:15 - 12:00 | Setup, Prompt Basics & Model Parameters | Hands-on |
| 12:00 - 13:00 | Lunch Break | - |
| 13:00 - 14:00 | Lab 1-2: API Call + Prompt to JSON | Hands-on |
| 14:00 - 14:45 | Lab 3: Factory Issue Analyzer & Web UI | Hands-on |
| 14:45 - 15:00 | Break | - |
| 15:00 - 15:30 | Lab 4: Factory Issue Batch Excel | Hands-on |
| 15:30 - 15:50 | Lab 5: Mini Challenge | Activity |
| 15:50 - 16:00 | Wrap-up & Next Step | Summary |

---

# ส่วนที่ 1
## Introduction & Course Objective

---

## เป้าหมายของคอร์สนี้

หลังจบคอร์สนี้ ผู้เรียนจะสามารถสร้าง **Mini AI Agent Prototype** ได้ด้วยตัวเอง เช่น

- ระบบวิเคราะห์ปัญหาเครื่องจักรขัดข้อง
- ระบบจัดหมวดหมู่รอยตำหนิสินค้า (QA)
- ระบบวิเคราะห์ความปลอดภัย (Safety)
- โปรแกรมสรุปข้อมูลอัตโนมัติลงตาราง Excel

โดยใช้ Microsoft Foundry + VS Code + Python และ **Streamlit** สำหรับหน้าเว็บแอปอย่างง่าย

---

## แนวคิดหลักของคอร์ส

```text
User Input / Excel Data
    |
    v
Python Application (Streamlit / Pandas)
    |
    v
Prompt
    |
    v
Microsoft Foundry Endpoint + API Key
    |
    v
AI Model
    |
    v
Response --> หน้าเว็บแอปพลิเคชันสวยงาม / ตาราง Excel สรุปผล
```

---

## สิ่งที่ "ไม่ใช่" เป้าหมายของคอร์สนี้

- ยังไม่ใช่ RAG Chatbot เต็มรูปแบบ
- ยังไม่ใช่ M365 Low-code Agent
- ยังไม่เชื่อมต่อ Production System จริงแบบอัตโนมัติ

คอร์สนี้คือ **พื้นฐาน** เพื่อให้เห็นภาพรวมและจุดประกายไอเดียการนำ AI ไปใช้ในแผนกตนเอง

---

# ส่วนที่ 2
## Microsoft Foundry & API Concept

---

## คำศัพท์สำคัญ

| คำ | ความหมายแบบง่าย |
|---|---|
| Project | พื้นที่ทำงานใน Foundry |
| Model | AI model ที่ใช้ประมวลผลข้อความ |
| Deployment | การนำ model มาเปิดให้เรียกใช้งาน |
| Endpoint | URL ที่โปรแกรมส่ง request ไปหา AI |
| API Key | รหัสลับสำหรับยืนยันสิทธิ์ |
| API Version | เวอร์ชันของ API ที่ endpoint รองรับ |

---

# ส่วนที่ 3
## API Key Security & Token Basics

---

## ทำไมต้องใช้ `.env`

ไม่ควรเขียน API Key ลงใน code โดยตรง

```python
# ทำแบบนี้เพื่อความปลอดภัย
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("AZURE_OPENAI_API_KEY")
```

---

## Token คืออะไร

Token คือหน่วยย่อยของข้อความที่ AI ใช้ประมวลผล ทั้ง input และ output

```text
Input Tokens + Output Tokens = Total Usage
```

**ทำไมต้องสนใจ:**
- ค่าใช้จ่ายและความเร็วในการตอบ
- การออกแบบ prompt ให้กระชับและชัดเจน

---

# ส่วนที่ 4
## Setup, Prompt Basics & Model Parameters

---

## Model Parameters: ควบคุมสมอง AI

ในการเขียนโปรแกรมเรียก AI เราสามารถตั้งค่า **Parameters** เพื่อควบคุมพฤติกรรมได้:

- **Temperature (0.0 - 2.0):** ค่าความสร้างสรรค์
  - `0.0`: ตรงไปตรงมา คาดเดาได้ (Deterministic) -> **เหมาะกับงานโรงงาน, สกัด JSON, จัดหมวดหมู่**
  - `0.7`: สร้างสรรค์ ยืดหยุ่น -> **เหมาะกับงานคิดไอเดีย, ร่างอีเมล**
- **Max Tokens:** จำกัดความยาวคำตอบ เพื่อควบคุมงบประมาณไม่ให้บานปลาย

---

## Setup เครื่อง (5 ขั้นตอน)

```bash
# 1. สร้าง virtual environment
python -m venv .venv
.\.venv\Scripts\Activate.ps1   # Windows PowerShell

# 2. ติดตั้ง package
pip install -r requirements.txt

# 3. สร้างไฟล์ .env จาก .env.example แล้วกรอกค่าจากผู้สอน
```

แพ็คเกจที่จะใช้หลักๆ: `openai`, `python-dotenv`, `streamlit`, `pandas`, `openpyxl`

---

## Prompt Structure

Prompt ที่ดีควรระบุให้ชัดว่า AI ต้องรับบทบาทอะไร ทำอะไร ใช้กติกาแบบไหน และตอบกลับรูปแบบใด

```text
Role:   AI ต้องรับบทบาทอะไร
Task:   ต้องทำอะไร
Context: ข้อมูลประกอบคืออะไร
Rules:  ข้อกำหนดหรือข้อห้าม
Output Format: ต้องตอบกลับเป็นรูปแบบใด
Input:  ข้อมูลดิบที่ให้วิเคราะห์
```

---

## Few-Shot Prompting (เทคนิคการให้ตัวอย่าง)

ในงานโรงงานที่มีคำศัพท์เฉพาะเจาะจง การอธิบายด้วยกฎอาจไม่พอ! การให้ตัวอย่าง (Examples) ควบคู่ไปด้วย จะทำให้ AI ทำงานได้ถูกต้องแม่นยำขึ้นมหาศาล

**Zero-Shot (ไม่มีตัวอย่าง):** 
*"จัดหมวดหมู่ปัญหานี้ให้หน่อย: ปั๊มลมมีน้ำมันรั่ว"*

**Few-Shot (มีตัวอย่าง):** 
*"ตัวอย่างที่ 1: ปั๊มลมมีน้ำมันรั่ว -> Category: Mechanical*
*ตัวอย่างที่ 2: เซ็นเซอร์ไฟหน้าจอไม่ติด -> Category: Electrical*
*ปัญหา: สายพานมอเตอร์ขาด -> Category: ???"*

---

# ส่วนที่ 5
## Lab 1-2: API Call และ Prompt to JSON

---

## ทำไมต้องให้ AI ตอบเป็น JSON

JSON คือรูปแบบที่ **โปรแกรมอ่านต่อได้ทันที** ทำให้สามารถเอาไปทำสี ทำการ์ดโชว์บนเว็บ หรือใส่ลงตาราง Excel ได้ง่าย

```python
response = client.chat.completions.create(
    model=deployment_name,
    messages=[ ... ],
    response_format={ "type": "json_object" } # บังคับเป็น JSON เสมอ
)
```

**ลองรัน Lab 1 และ Lab 2:**
```bash
python workshops/lab-01-first-api-call/starter.py
python workshops/lab-02-prompt-to-json/starter.py
```

---

# ส่วนที่ 6
## Lab 3: Factory Issue Analyzer & Web UI

---

## Human-in-the-Loop (คนตรวจสอบเสมอ!)

ในการทำงานจริงที่เกี่ยวข้องกับความปลอดภัยและสายการผลิต **เราไม่ควรให้ AI ตัดสินใจบันทึกข้อมูลหรือสั่งการเอง 100% โดยไม่มีคนตรวจ**

**การออกแบบที่ดี:**
1. ให้ AI วิเคราะห์และกรอกข้อมูลลงช่องให้ (Pre-fill)
2. พนักงาน (Human) อ่านทบทวนและสามารถแก้ไขได้
3. พนักงานกดยืนยัน (Submit) เพื่อบันทึกเข้าระบบ

```bash
# รันหน้าเว็บ UI
cd workshops/lab-03-factory-issue-analyzer
streamlit run app_streamlit.py
```

---

# ส่วนที่ 7
## Lab 4: Factory Issue Batch Excel

---

## ประมวลผลจำนวนมากด้วย Pandas & Error Handling

เมื่อต้องประมวลผลข้อมูลใน Excel ทีละ 1,000 แถว **API อาจจะตอบกลับผิดพลาด หรืออินเทอร์เน็ตอาจจะหลุดชั่วคราว**

เราต้องใช้ `try-except` ใน Python เพื่อไม่ให้โปรแกรมพังกลางคัน:
```python
try:
    ai_result = analyze_issue(row['issue_report'])
except Exception as e:
    print(f"เกิดข้อผิดพลาด: {e}")
    ai_result = {"category": "Error", "priority": "Error", "summary": "Error"}
```

```bash
cd workshops/lab-04-factory-issue-batch-excel
python starter.py
```

เช็คผลลัพธ์ไฟล์ Excel ที่ถูกสร้างขึ้น! บรรทัดไหนพัง โปรแกรมจะข้ามไปทำบรรทัดต่อไปอย่างปลอดภัย

---

# ส่วนที่ 8
## Lab 5: Mini Challenge

---

## เลือก Use Case ของตัวเอง

ทดลองนำความรู้ที่เรียนทั้งหมดมาประยุกต์ใช้กับงานในแผนกของคุณ
1. คิดปัญหาที่พบเจอบ่อย (QA, Maintenance, Safety, Logistics)
2. แก้ไขไฟล์ `starter.py` หรือหน้าเว็บ `app_streamlit.py`
3. เขียน Prompt กำหนดกติกา และ Output (JSON) ใหม่

---

# ขอบคุณครับ/ค่ะ
## Q&A

ทดลองต่อได้ที่โฟลเดอร์ `workshops/` และสามารถต่อยอดไปใช้ในแผนกได้เลย!
