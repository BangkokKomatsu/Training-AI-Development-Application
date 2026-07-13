# Lab 5 - Mini Challenge

## Goal

ให้ผู้เรียนออกแบบ Use Case และ Prompt ของตนเอง แล้วทดลองรันเป็นเว็บแอปพลิเคชันด้วย Streamlit เพื่อให้สามารถนำไปเสนอเป็นไอเดียใช้งานจริงในแผนกตนเองได้

## ตัวอย่างอ้างอิง (Reference Examples)

ก่อนเริ่มออกแบบ Use Case ของตัวเอง ลองเปิดไฟล์เหล่านี้ดูเป็นแนวทางว่า prompt และหน้าเว็บที่ดีหน้าตาเป็นอย่างไร (รันได้เหมือน `app_streamlit_template.py`):

- `reference_procurement.py` - AI ตรวจสอบคำขอซื้อว่าข้อมูลครบก่อนส่งอนุมัติหรือไม่ (งานจัดซื้อ)
- `reference_production_planning.py` - AI สรุปบันทึกหน้างานประจำวันให้ทีมวางแผนการผลิต (งานวางแผนการผลิต)
- `reference_safety_checklist.py` - AI ตรวจสอบความพร้อมด้านความปลอดภัย**ก่อน**เริ่มงาน (งาน Safety มุม pre-work checklist — คนละมุมกับตัวเลือกข้อ 2 ด้านล่างที่เป็นการจัดหมวดหมู่อุบัติเหตุที่**เกิดขึ้นแล้ว** จึงยังเลือกทำข้อ 2 เป็น mini challenge ได้ตามปกติ)

```bash
streamlit run workshops/lab-05-mini-challenge/reference_procurement.py
streamlit run workshops/lab-05-mini-challenge/reference_production_planning.py
streamlit run workshops/lab-05-mini-challenge/reference_safety_checklist.py
```

ไฟล์เหล่านี้เป็น**ตัวอย่างสำเร็จรูป** ไม่ใช่โจทย์ที่ต้องเลือกทำ (หัวข้อของคุณเองให้เลือกจากลิสต์ด้านล่าง)

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
