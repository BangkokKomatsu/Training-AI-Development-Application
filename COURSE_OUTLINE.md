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
- เทคนิค Few-Shot Prompting การใส่ตัวอย่างข้อความเพื่อให้ AI เข้าใจบริบทศัพท์เทคนิคในโรงงานมากขึ้น
- วิธีการตั้งค่าพารามิเตอร์โมเดล (Temperature & Max Tokens) เพื่อควบคุมความแม่นยำและความคิดสร้างสรรค์
- วิธีให้ AI ตอบกลับเป็น JSON อย่างแม่นยำ
- วิธีเขียนโค้ดรองรับข้อผิดพลาด (Error Handling & API Resilience) เพื่อไม่ให้สคริปต์หยุดทำงานเมื่อเน็ตหลุดหรือข้อมูลผิดพลาด
- วิธีสร้างหน้าเว็บแอปอย่างง่ายด้วย Streamlit พร้อมการออกแบบแบบ Human-in-the-Loop เพื่อให้พนักงานมีโอกาสตรวจสอบผลลัพธ์จาก AI ก่อนกดยืนยันใช้งานจริง
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

---

## 10. Slide Deck Outline (สำหรับให้ AI สร้างไฟล์ PPTX)

*ข้อมูลส่วนนี้ออกแบบมาเพื่อให้คุณนำไปคัดลอกวาง (Copy & Paste) ลงในเครื่องมือสร้างสไลด์ด้วย AI หรือใช้เป็นโครงร่างในการทำสไลด์นำเสนอได้อย่างรวดเร็ว*

**Slide 1: Title Slide**
- **Title:** พัฒนา AI Application เบื้องต้น
- **Subtitle:** สร้าง Mini AI Agent ด้วย Microsoft Foundry, API Key และ Prompt
- **Presenter:** [Thitiwut S.]

**Slide 2: Course Objective (เป้าหมายหลักสูตร)**
- ทำความเข้าใจการทำงานเบื้องหลังของ AI (API & Token)
- เรียนรู้วิธีการส่งคำสั่ง (Prompt Engineering) ให้ได้ผลลัพธ์ที่ต้องการแบบอัตโนมัติ
- สร้าง AI Application ต้นแบบเพื่อประยุกต์ใช้ในโรงงานและการทำงานจริง
- ไม่ใช่แค่พิมพ์คุยกับ ChatGPT แต่คือการ "นำ AI ไปฝังในระบบ"

**Slide 3: ทำไม AI ถึงสำคัญในยุคอุตสาหกรรม? (Why AI in Manufacturing?)**
- **ลดเวลาทำงานซ้ำซ้อน (Automate Repetitive Tasks):** ให้ AI ช่วยสรุปรายงานหรือคัดแยกปัญหา
- **ลดความผิดพลาด (Reduce Human Error):** AI สามารถตรวจสอบ Log ข้อมูลจำนวนมหาศาลโดยไม่เหนื่อยล้า
- **เพิ่มขีดความสามารถ (Augment Human Capability):** เป็นผู้ช่วยคิดและวางแผน (Co-pilot) ไม่ใช่มาแทนที่คน
- **ก้าวสู่ Smart Factory:** การเชื่อมต่อข้อมูลหน้างานเข้ากับสมองกลเพื่อการตัดสินใจแบบ Real-time

**Slide 4: วิวัฒนาการสู่ Generative AI (The Rise of GenAI)**
- **Traditional AI:** เก่งเรื่องตัวเลข สถิติ และการทำนายแนวโน้ม (Predictive)
- **Generative AI (GenAI):** มีความสามารถในการ "สร้างใหม่" (ข้อความ, รูปภาพ, โค้ด)
- **Large Language Model (LLM):** โมเดลภาษาขนาดใหญ่ที่ถูกฝึกมาให้อ่านและเขียนภาษาได้เหมือนมนุษย์ (เช่น ตระกูล GPT)
- จุดเปลี่ยนสำคัญที่ทำให้ AI เข้าถึงคนทำงานทุกระดับ ไม่ใช่แค่สาย Tech

**Slide 5: จากหน้า Chat สู่ Application (From Chat to App)**
- **Web Chat (เช่น ChatGPT):** เหมาะสำหรับ Personal Productivity (พิมพ์ถาม-ตอบด้วยคน)
- **API (Application Programming Interface):** ช่องทางเชื่อมต่อให้ "ระบบคุยกับระบบ"
- การสร้าง AI Application คือการใช้ API เพื่อดึงความฉลาดของ AI ไปฝังไว้ในแอปพลิเคชันของเรา (เช่น Streamlit, Excel หรือ ERP ของบริษัท) โดยไม่ต้องมีคนมานั่งพิมพ์

**Slide 6: What is Microsoft Foundry?**
- แพลตฟอร์ม AI ระดับองค์กร (Enterprise AI Platform) ของ Microsoft
- มีความปลอดภัยสูง ข้อมูลบริษัทจะไม่ถูกนำไป Train โมเดลสาธารณะต่อ (Data Privacy & Security)
- อนุญาตให้นักพัฒนาเรียกใช้งานโมเดลชั้นนำ (เช่น GPT-4o) ผ่านระบบ Cloud ของ Azure

**Slide 7: Key Concepts & Cost Estimation (คำศัพท์และค่าใช้จ่าย)**
- **Endpoint:** URL ที่อยู่ของโมเดล (เหมือนที่อยู่ตู้ไปรษณีย์)
- **API Key:** กุญแจยืนยันตัวตน (ห้ามหลุดสู่สาธารณะเด็ดขาด)
- **Deployment Name:** ชื่อรุ่นของโมเดลที่เราตั้งไว้ใช้งาน (เช่น gpt-5-mini)
- **Token & Cost:** หน่วยนับคำของ AI (1 Token ≈ 0.75 คำไทย) การคิดราคาจะนับรวม Input + Output Tokens ควรระวังเรื่อง Rate Limit (ข้อจำกัดการเรียกใช้งานต่อนาที)

**Slide 8: Security First & Human-in-the-Loop**
- ❌ **ห้าม** อัปโหลดข้อมูลที่เป็นความลับ (Confidential, Trade Secrets, สูตรการผลิต)
- ❌ **ห้าม** แชร์ API Key ลงในกลุ่ม Line หรือใส่ไว้ในโค้ดดิบแบบสาธารณะ
- ✅ **ควร** บันทึก API Key ไว้ในไฟล์ `.env` ที่ปลอดภัย
- ✅ **Human-in-the-Loop:** ห้ามให้ AI ตัดสินใจส่งคำสั่งควบคุมเครื่องจักรหรืออนุมัติเอกสารเองโดยไม่มีพนักงานตรวจสอบ (ต้องออกแบบให้คนกดยืนยันก่อนเสมอ)

**Slide 9: Workshop 1 - First API Call**
- **เป้าหมาย:** ทักทาย AI Model ด้วยภาษา Python
- **เครื่องมือ:** VS Code, Python, `.env`
- **Steps:** 
  1. เตรียม API Key และ Endpoint
  2. เขียนโค้ดส่งข้อความ "สวัสดี" หา AI
  3. สังเกตผลลัพธ์ (Response) ที่ได้กลับมาผ่าน Terminal

**Slide 10: Prompt Engineering & Parameters**
- การเขียน Prompt สำหรับโปรแกรมเมอร์ ต้องสั่งให้ AI ตอบเป็น **"โครงสร้างข้อมูล" (Structured Output)**
- **โครงสร้าง Prompt ที่ดี:** Role, Rules, Context, Output Format, Input
- **Few-Shot Prompting:** การใส่ตัวอย่างข้อความปัญหาและ JSON ผลลัพธ์ที่ต้องการลงไป 1-2 ตัวอย่าง เพื่อให้ AI ทำงานได้แม่นยำขึ้นมาก
- **Temperature:** การตั้งค่าความสร้างสรรค์ `Temperature = 0.0` (ทำงานตรงไปตรงมา ไม่มั่ว เหมาะกับงานจัดกลุ่ม), `Temperature = 0.7` (เหมาะกับร่างอีเมลหรือคิดไอเดีย)

**Slide 11: Workshop 2 - Prompt to JSON**
- **เป้าหมาย:** บังคับให้ AI ส่งข้อมูลกลับมาเป็น JSON เสมอ
- **ทำไมต้อง JSON?:** เพราะโปรแกรมคอมพิวเตอร์และระบบฐานข้อมูลสามารถอ่านค่า JSON และเอาไปทำงานต่อได้ง่าย
- **สิ่งที่จะได้ทำ:** ดึงฟิลด์ "หมวดหมู่ปัญหา" และ "ความเร่งด่วน" ออกมาจากข้อความร้องเรียนยาวๆ

**Slide 12: Workshop 3 - Factory Issue Analyzer & Web UI**
- **เป้าหมาย:** สร้างแอปพลิเคชันจริง มีปุ่มกด มีหน้าเว็บ และปลอดภัย
- **เครื่องมือ:** Streamlit
- **สิ่งที่จะได้ทำ:**
  - วิเคราะห์ Log ปัญหาเครื่องจักรแบบอัตโนมัติ แสดงผลลัพธ์ในการ์ดสีต่างๆ
  - **Human-in-the-Loop:** นำผลลัพธ์ของ AI มาใส่ในกล่องข้อความให้ผู้ใช้งานแก้ไขก่อนกดยืนยันเซฟ

**Slide 13: Workshop 4 - Excel Batch & Error Handling**
- **เป้าหมาย:** ประมวลผลข้อมูล 1,000 แถวอัตโนมัติอย่างปลอดภัย ไม่ให้โปรแกรมพังกลางคัน
- **เครื่องมือ:** Pandas และบล็อก `try-except` ใน Python
- **สิ่งที่จะได้ทำ:** 
  - อัปโหลดไฟล์ Excel -> AI อ่านทีละบรรทัด -> เขียนผลลัพธ์กลับลง Excel
  - ดักจับ API Error หรือ JSON ผิดรูปแบบ หากบรรทัดไหนพัง ให้บันทึกเป็น Error แล้วข้ามไปทำบรรทัดถัดไปโดยอัตโนมัติ

**Slide 14: Mini Challenge - Your Turn!**
- **เป้าหมาย:** ลองทำแอปพลิเคชันของแผนกคุณเอง
- **คำแนะนำ:** 
  - เลือกปัญหาที่ต้องวิเคราะห์ข้อมูลซ้ำๆ (Defect QA, ข้อร้องเรียนพนักงาน, ใบบันทึกความปลอดภัย)
  - ใช้ `app_streamlit_template.py` เปลี่ยนแค่ Prompt และชื่อฟิลด์
  - เตรียมนำเสนอให้เพื่อนในคลาสดู!

**Slide 15: Next Steps (ก้าวต่อไป)**
- **RAG (Retrieval-Augmented Generation):** ทำให้ AI ค้นหาและตอบคำถามจากคู่มือบริษัท PDF หรือฐานข้อมูลขององค์กร
- **M365 Copilot / Power Platform:** การสร้าง Agent แบบ Low-code/No-code 
- **Let's Build:** พร้อมแล้วไปเปิด VS Code และเริ่มทำ Lab 1 กันเลย!
