# Course Outline

## AI Application Development: Build Your First Mini AI Agent with Microsoft Foundry

**ชื่อภาษาไทย:** พัฒนา AI Application เบื้องต้น: สร้าง Mini AI Agent ด้วย Microsoft Foundry, API Key, Token และ Prompt  
**ระยะเวลา:** 1 วัน เวลา 10:00 - 16:00  
**รูปแบบ:** Lecture + Demo + Hands-on Workshop  
**เครื่องมือหลัก:** Microsoft Foundry, VS Code, Python, Streamlit

---

## 1. ภาพรวมหลักสูตร

หลักสูตรนี้ออกแบบสำหรับผู้ที่ต้องการเริ่มต้นสร้าง AI Application หรือ Mini AI Agent Prototype โดยใช้ Microsoft Foundry ที่ BKC เตรียมไว้ให้ ผู้เรียนจะได้เรียนรู้แนวคิดของ API Key, Endpoint, Deployment, Token และ Prompt พร้อมลงมือเขียน Python บน VS Code เพื่อเรียกใช้งาน AI Model ผ่าน API

ผู้เรียนจะได้ทดลองสร้าง Mini AI Agent แบบง่าย เช่น การตรวจจับปัญหาเครื่องจักรขัดข้อง, การวิเคราะห์รอยตำหนิสินค้า, และการอ่านรายงานความปลอดภัย โดยเน้นความเข้าใจพื้นฐาน การสร้างหน้าเว็บแอปพลิเคชันอย่างง่ายด้วย Streamlit และเห็นผลลัพธ์จริงภายในวันอบรม

---

## 2. เหมาะกับใคร

- พนักงานภายใน BKC เช่น ฝ่ายผลิต, ซ่อมบำรุง, QA, ความปลอดภัย, คลังสินค้า, IT, หรือ Supplier Coordinator
- ผู้ที่เคยใช้งาน ChatGPT / Copilot / Gemini ผ่านหน้าเว็บ และต้องการเข้าใจการใช้งานผ่าน API
- ผู้ที่ต้องการเข้าใจการสร้าง Mini AI Agent Prototype และหน้าเว็บแอปพลิเคชันอย่างง่าย ก่อนต่อยอดไป RAG Chatbot หรือ M365 AI Agent

---

## 3. พื้นฐานผู้เข้าอบรม

- ใช้งานคอมพิวเตอร์และอินเทอร์เน็ตได้คล่อง
- เข้าใจการใช้งานไฟล์และโฟลเดอร์บน Windows
- มีพื้นฐานการใช้งาน VS Code หรือพร้อมเรียนรู้ในวันอบรม
- เคยเห็น Python เบื้องต้นจะช่วยให้เรียนได้เร็วขึ้น แต่ไม่จำเป็นต้องเป็น programmer เต็มตัว
- อ่านตัวอย่างภาษาอังกฤษพื้นฐานใน Prompt และ Response ได้บ้าง

---

## 4. ผู้เข้าอบรมต้องเตรียม

- Notebook ส่วนตัว พร้อม internet
- ติดตั้ง VS Code
- ติดตั้ง Python 3.10 ขึ้นไป
- ติดตั้ง Git หากต้องการ clone repository
- ได้รับ API Key, Endpoint และ Deployment Name จากผู้สอนหรือ BKC ก่อนเริ่ม workshop
- ข้อมูลตัวอย่างที่ไม่ใช่ข้อมูลจริงหรือข้อมูลลับ

> หมายเหตุ: ห้ามใช้ข้อมูล Confidential, Customer Data, Contract, ราคา, Personal Data หรือ API Key ส่วนตัวใน workshop

---

## 5. สิ่งที่จะได้เรียนรู้

- AI Application และ Mini AI Agent คืออะไร
- Microsoft Foundry เกี่ยวข้องกับ AI API อย่างไร
- ความหมายของ Endpoint, API Key, Deployment Name และ Model
- Token คืออะไร และมีผลต่อค่าใช้จ่าย/ข้อจำกัดอย่างไร
- วิธีเก็บ API Key อย่างปลอดภัยด้วย `.env`
- วิธีตั้งค่า VS Code + Python สำหรับเรียก AI API
- วิธีเขียน Prompt แบบ Role, Task, Context, Rules, Output Format และ Input
- วิธีให้ AI ตอบกลับเป็น JSON อย่างแม่นยำ
- วิธีสร้างหน้าเว็บแอปอย่างง่ายด้วย Streamlit เพื่อแสดงผลลัพธ์จาก AI (ทำกล่องข้อความ การ์ดสี สรุปผลลัพธ์)
- วิธีอ่านข้อมูลและเขียนผลวิเคราะห์กลับลงไฟล์ Excel (Pandas + Openpyxl) สำหรับประมวลผลเป็นกลุ่ม (Batch)

---

## 6. Workshop ที่จะได้ทำ

| Lab | ชื่อกิจกรรม | สิ่งที่ผู้เรียนจะได้ทำ | ผลลัพธ์ที่ได้ |
|---|---|---|---|
| Lab 1 | First API Call | ตั้งค่า `.env` และเรียก AI Model ผ่าน Microsoft Foundry | ได้ Response แรกจาก AI API |
| Lab 2 | Prompt to JSON | ปรับ Prompt ให้ AI ตอบเป็น JSON | เข้าใจ Structured Output |
| Lab 3 | Factory Issue Analyzer & Web UI | สร้างระบบวิเคราะห์ปัญหาในโรงงาน (ผลิต/ซ่อมบำรุง/QA/ความปลอดภัย) พร้อมเชื่อมหน้าเว็บ **Streamlit** | เว็บแอปพลิเคชัน AI วิเคราะห์ปัญหาโรงงานแบบเห็นภาพ |
| Lab 4 | Factory Issue Batch & Excel | เขียนโค้ดวนลูปวิเคราะห์ปัญหาหลายเคสจากตารางข้อมูล และบันทึกผลกลับลงในไฟล์ **Excel** | โปรแกรม AI ช่วยจัดกลุ่มและจัดการรายงานใน Excel อัตโนมัติ |
| Lab 5 | Mini Challenge | ออกแบบ Prompt และต่อยอด UI บนหน้าเว็บ Streamlit ของตัวเอง | โปรเจกต์ Prototype ที่สามารถนำกลับไปใช้งานจริงที่แผนกได้ |

### Bonus Labs (เสริม ถ้ามีเวลาเหลือ)

| Lab | ชื่อกิจกรรม | สิ่งที่ผู้เรียนจะได้ทำ | ผลลัพธ์ที่ได้ |
|---|---|---|---|
| Lab 6 | Multi-turn Chatbot | สร้าง Chatbot ที่เก็บ conversation history | เข้าใจ Memory และผลต่อ Token |
| Lab 7 | Function Calling | ให้ AI เรียกฟังก์ชัน Python เพื่อดึงข้อมูลจาก mock database | พื้นฐานก่อนต่อยอดไป Agent ที่เชื่อมระบบจริง |

> เนื้อหาเพิ่มเติม: `docs/07-prompt-engineering-advanced.md`, `docs/08-multi-turn-conversation.md`, `docs/09-function-calling.md`
> สไลด์สำหรับนำเสนอทั้งคอร์ส (รวม Bonus): `slides/course-slides.md`

---

## 7. Agenda เบื้องต้น เวลา 10:00 - 16:00

| เวลา | หัวข้อ | รูปแบบ | รายละเอียด |
|---|---|---|---|
| 10:00 - 10:20 | Introduction & Course Objective | Lecture | แนะนำเป้าหมายหลักสูตร ภาพรวม Mini AI Agent และหน้าเว็บแอปที่จะได้สร้าง |
| 10:20 - 10:50 | AI Application, Microsoft Foundry & API Concept | Lecture + Demo | อธิบาย Foundry, Endpoint, Deployment, API Key, Request และ Response |
| 10:50 - 11:15 | API Key Security & Token Basics | Lecture | วิธีเก็บ Key, ความหมายของ Token และข้อควรระวัง |
| 11:15 - 12:00 | VS Code + Python Setup & Prompt Basics | Hands-on | ตั้งค่า project, `.env`, package และเขียน Prompt พื้นฐาน |
| 12:00 - 13:00 | Lunch Break | - | - |
| 13:00 - 13:30 | Workshop 1: First API Call | Hands-on Lab | เรียก AI Model ผ่าน Microsoft Foundry ด้วย Python |
| 13:30 - 14:00 | Workshop 2: Structured Output & JSON | Hands-on Lab | ให้ AI ตอบกลับเป็น JSON เพื่อนำไปใช้ต่อในโค้ด |
| 14:00 - 14:45 | Workshop 3: Factory Issue & Streamlit UI | Hands-on Lab | วิเคราะห์ปัญหาโรงงาน และสร้างหน้าเว็บอินเทอร์เฟซด้วย Streamlit |
| 14:45 - 15:00 | Break | - | - |
| 15:00 - 15:30 | Workshop 4: Excel Batch Processing | Hands-on Lab | วนลูปอ่านข้อมูล ประมวลผลด้วย AI และบันทึกผลการคัดแยกประเภทกลับลง Excel |
| 15:30 - 15:50 | Mini Challenge: Design Your Own Use Case | Activity | ผู้เรียนออกแบบ Prompt และต่อยอด UI บนหน้าเว็บ Streamlit ของตนเอง |
| 15:50 - 16:00 | Wrap-up, Security Checklist & Next Step | Summary | สรุปสิ่งที่เรียนและแนวทางต่อยอด |

---

## 8. ขอบเขตของคอร์สนี้

| ครอบคลุมในคอร์สนี้ | ยังไม่ลงลึกในคอร์สนี้ |
|---|---|
| API Key, Endpoint, Token และ Prompt | RAG Chatbot จากเอกสารจำนวนมาก |
| การเรียก AI API ด้วย Python | Agent เต็มรูปแบบที่เชื่อมหลายระบบ |
| การรับ Response เป็น Text / JSON | Production-grade deployment |
| หน้าเว็บแอปพลิเคชันอย่างง่าย (Streamlit) | Governance ระดับองค์กรแบบเต็มรูปแบบ |
| การเขียนผลลัพธ์เป็นตาราง Excel | การเชื่อมต่อฐานข้อมูลจริง |
| Security เบื้องต้นสำหรับ API Key | |

---

## 9. หมายเหตุสำหรับผู้จัดอบรม

- BKC ควรเตรียม Microsoft Foundry project, model deployment, endpoint และ API key ก่อนวันอบรม
- ควรกำหนด quota และ rate limit ให้เหมาะสมกับจำนวนผู้เรียน
- ควรเตรียม `.env.example` และ sample data โดยไม่ใส่ key จริง
- ควรติดตั้งแพ็คเกจเสริม (Streamlit, Pandas, Openpyxl) ในเครื่องผู้เรียนหรือมีอินเทอร์เน็ตที่พร้อมติดตั้ง
- ควรทดสอบ workshop ทุก Lab ก่อนวันอบรม
- หลังอบรมควร revoke หรือ rotate API Key ที่ใช้ร่วมกันในห้องเรียน
