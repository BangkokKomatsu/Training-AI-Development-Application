# Lab 5 - Mini Challenge

## Goal

ให้ผู้เรียนออกแบบ Use Case และ Prompt ของตนเอง แล้วทดลองรันเป็นเว็บแอปพลิเคชันด้วย Streamlit เพื่อให้สามารถนำไปเสนอเป็นไอเดียใช้งานจริงในแผนกตนเองได้

## Choose One Use Case

ลองเลือกไอเดียเหล่านี้ หรือคิด Use Case ของแผนกคุณเอง:
1. QC Defect Analyzer (วิเคราะห์รอยตำหนิสินค้าและแยกประเภท)
2. Safety Incident Classifier (วิเคราะห์รายงานอุบัติเหตุ/ความปลอดภัย)
3. Maintenance Work Order Generator (แปลงข้อความแจ้งซ่อมเป็นใบสั่งงาน)
4. Logistics Delay Summarizer (สรุปปัญหาสินค้าล่าช้า)
5. Meeting Note to Action Plan (สรุปรายงานการประชุมโรงงานเป็น Action Plan)

## Task

แก้ไขไฟล์ `app_streamlit_template.py` โดยกำหนด:

- เปลี่ยนชื่อแอป `st.title(...)` และคำอธิบายให้เข้ากับแผนกคุณ
- แก้ไขตัวแปร `prompt` ในฟังก์ชัน `analyze_custom_usecase`
  - กำหนด Role ของ AI
  - กำหนด Rules
  - ระบุชื่อฟิลด์ JSON ที่ต้องการให้ AI ส่งกลับมา
- (Optional) แก้ไขส่วน UI ในการดึงค่า `result` มาจัดรูปแบบใหม่ให้สวยงาม

## Run

```bash
streamlit run workshops/lab-05-mini-challenge/app_streamlit_template.py
```

## Presentation

สรุป 3 ข้อเพื่อนำเสนอให้เพื่อนในคลาสฟัง:

1. Use Case ของแผนกคุณคืออะไร
2. AI ช่วยลดเวลาหรือแก้ปัญหาอะไรให้คุณ
3. หน้าเว็บที่ทำเสร็จแล้วหน้าตาเป็นอย่างไร (เปิดให้ดู)
