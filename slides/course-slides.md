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
| 10:20 - 10:50 | ทำไม AI สำคัญ + Microsoft Foundry & API Concept | Lecture + Demo |
| 10:50 - 11:15 | API Key Security & Token Cost Estimation | Lecture |
| 11:15 - 12:00 | Setup, Prompt Basics & Model Parameters | Hands-on |
| 12:00 - 13:00 | Lunch Break | - |
| 13:00 - 13:25 | Lab 1: First API Call | Hands-on Lab |
| 13:25 - 14:00 | Lab 2: Prompt to JSON | Hands-on Lab |
| 14:00 - 14:45 | Lab 3: Factory Issue Analyzer & Web UI | Hands-on |
| 14:45 - 15:00 | Break | - |
| 15:00 - 15:30 | Lab 4: Factory Issue Batch Excel | Hands-on |
| 15:30 - 15:50 | Lab 5: Mini Challenge | Activity |
| 15:50 - 16:00 | Wrap-up, Security Checklist & Next Step | Summary |

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
## วิวัฒนาการ: จาก Manual สู่ GenAI API

---

## ทำไม AI ถึงสำคัญในยุคอุตสาหกรรม?

- **ลดเวลาทำงานซ้ำซ้อน (Automate Repetitive Tasks):** ให้ AI ช่วยสรุปรายงานหรือคัดแยกปัญหา
- **ลดความผิดพลาด (Reduce Human Error):** AI ตรวจสอบ Log ข้อมูลจำนวนมหาศาลโดยไม่เหนื่อยล้า
- **เพิ่มขีดความสามารถ (Augment Human Capability):** เป็นผู้ช่วยคิดและวางแผน (Co-pilot) ไม่ใช่มาแทนที่คน
- **ก้าวสู่ Smart Factory:** เชื่อมข้อมูลหน้างานเข้ากับสมองกลเพื่อการตัดสินใจแบบ Real-time

---

## Traditional AI vs Generative AI vs LLM

- **Traditional AI:** เก่งเรื่องตัวเลข สถิติ และการทำนายแนวโน้ม (Predictive)
- **Generative AI (GenAI):** มีความสามารถในการ "สร้างใหม่" (ข้อความ, รูปภาพ, โค้ด)
- **Large Language Model (LLM):** โมเดลภาษาขนาดใหญ่ที่ถูกฝึกให้อ่าน/เขียนภาษาได้เหมือนมนุษย์ (เช่น ตระกูล GPT)
- จุดเปลี่ยนสำคัญที่ทำให้ AI เข้าถึงคนทำงานทุกแผนก ไม่ใช่แค่สาย Tech

---

## จาก Chat สู่ Application (Chat → API)

- **Web Chat (เช่น ChatGPT):** เหมาะกับ Personal Productivity (คนพิมพ์ถาม-ตอบเอง)
- **API (Application Programming Interface):** ช่องทางให้ "ระบบคุยกับระบบ"
- การสร้าง AI Application คือการใช้ API ฝังความฉลาดของ AI เข้าแอปพลิเคชันของเรา (Streamlit, Excel, ERP) โดยไม่ต้องมีคนมานั่งพิมพ์

> 👉 **นี่คือสิ่งที่ Lab 1-5 ทั้งหมดในวันนี้กำลังจะทำ**

---

# ส่วนที่ 3
## Microsoft Foundry & API Concept

---

## คำศัพท์สำคัญ

Foundry คือแพลตฟอร์มที่เราจะไปเรียก API ตามที่เพิ่งเห็นในสไลด์ก่อนหน้า

| คำ | ความหมายแบบง่าย |
|---|---|
| Project | พื้นที่ทำงานใน Foundry |
| Model | AI model ที่ใช้ประมวลผลข้อความ |
| Deployment | การนำ model มาเปิดให้เรียกใช้งาน |
| Endpoint | URL ที่โปรแกรมส่ง request ไปหา AI |
| API Key | รหัสลับสำหรับยืนยันสิทธิ์ |
| API Version | เวอร์ชันของ API ที่ endpoint รองรับ |

---

# ส่วนที่ 4
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

# ส่วนที่ 5
## Setup, Prompt Basics & Model Parameters

---

## Model Parameters: ควบคุมสมอง AI

ในการเขียนโปรแกรมเรียก AI เราสามารถตั้งค่า **Parameters** เพื่อควบคุมพฤติกรรมได้:

- **Temperature (0.0 - 2.0):** ค่าความสร้างสรรค์
  - `0.0`: ตรงไปตรงมา คาดเดาได้ (Deterministic) -> **เหมาะกับงานโรงงาน, สกัด JSON, จัดหมวดหมู่**
  - `0.7`: สร้างสรรค์ ยืดหยุ่น -> **เหมาะกับงานคิดไอเดีย, ร่างอีเมล**
- **Max Tokens:** จำกัดความยาวคำตอบ เพื่อควบคุมงบประมาณไม่ให้บานปลาย

> ⚠️ **หมายเหตุรุ่นโมเดล:** ตระกูล **`gpt-5-mini`** (reasoning model) **ไม่รองรับ `temperature` และ `max_tokens`** (ใช้ `max_completion_tokens` แทน หรือไม่ต้องใส่) — พารามิเตอร์ข้างบนใช้ได้กับรุ่นอย่าง `gpt-4o` ส่วน gpt-5-mini คุมความแม่นยำด้วย **Prompt ที่ชัด + JSON mode**

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

# ส่วนที่ 6
## Lab 1: First API Call

---

## เรียก AI ผ่านโค้ดครั้งแรก (Request → Response)

ย้อนกลับไปดู diagram ในส่วนที่ 1: `App → Prompt → Foundry Endpoint + Key → AI Model → Response` — นี่คือโค้ดจริงของ diagram นั้น

```python
response = client.chat.completions.create(
    model=deployment_name,
    messages=[
        {"role": "system", "content": "You are a helpful AI assistant."},
        {"role": "user", "content": "Explain what an API key is in simple Thai language."},
    ],
)
print(response.choices[0].message.content)
```

```bash
python workshops/lab-01-first-api-call/starter.py
```

---

## ลองเอง: Lab 1

1. เปิด `starter.py` แก้ข้อความใน `content` (บรรทัด 19) เป็นคำถามอื่น แล้วรันใหม่
2. เปิด `solution.py` ดูว่ายกระดับไปอีกขั้นด้วย `input()` ให้พิมพ์คำถามสดในหน้าจอได้เลย ไม่ต้องแก้โค้ดทุกครั้ง

---

# ส่วนที่ 7
## Lab 2: Prompt to JSON

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

```bash
python workshops/lab-02-prompt-to-json/starter.py
```

---

## ลองเอง: Lab 2

1. แก้ `issue_report` (บรรทัด 16) เป็นปัญหาอื่น แล้วรันใหม่
2. เปิดคอมเมนต์ Step 2-3 ใน `starter.py` (parse JSON ด้วย `json.loads` + ตัดสินใจตาม `priority`) แล้วรันดูผลลัพธ์ที่เปลี่ยนไป

---

# ส่วนที่ 8
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

# ส่วนที่ 9
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

## ลองเอง: Lab 4

เพิ่มเคสปัญหาใหม่ใน `sample-data/factory_issues.json` แล้วรันซ้ำ ดูว่าไฟล์ Excel ที่ได้เปลี่ยนไปตามที่คาดไว้ไหม

---

# ส่วนที่ 10
## Lab 5: Mini Challenge

---

## เลือก Use Case ของตัวเอง

ทดลองนำความรู้ที่เรียนทั้งหมดมาประยุกต์ใช้กับงานในแผนกของคุณ
1. คิดปัญหาที่พบเจอบ่อย (QA, Maintenance, Safety, Logistics)
2. แก้ไขไฟล์ `starter.py` หรือหน้าเว็บ `app_streamlit.py`
3. เขียน Prompt กำหนดกติกา และ Output (JSON) ใหม่

---

# ส่วนที่ 11
## Security Checklist ก่อนใช้งานจริง

---

## สิ่งที่ต้องระวังก่อนนำไปใช้งานจริง

- ❌ **ห้ามใช้ข้อมูล:** Customer data, Personal data, Contract, ราคา, ข้อมูลการเงิน, สูตร/ข้อมูลลับเครื่องจักร, เอกสารภายในที่ไม่ได้รับอนุญาต
- ❌ **ห้าม hard-code API Key** ในไฟล์หรือ commit ขึ้น git — ใช้ `.env` + `.gitignore` เท่านั้น
- ✅ **Human Review เสมอ** โดยเฉพาะ: สั่งควบคุมเครื่องจักร, ตัดสิน quality issue, สรุปเอกสารสำคัญ, business decision
- ⚠️ **Prototype Limitation:** Mini AI Agent วันนี้เป็น prototype เพื่อการเรียนรู้ ยังไม่ใช่ production system
- 🔁 หลังจบคอร์ส API Key ที่ใช้ร่วมกันในห้องเรียนจะถูก rotate/revoke

---

# ขอบคุณครับ/ค่ะ
## Q&A

ทดลองต่อได้ที่โฟลเดอร์ `workshops/` และสามารถต่อยอดไปใช้ในแผนกได้เลย!
