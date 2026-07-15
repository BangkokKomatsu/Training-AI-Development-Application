# Lab 4 - Factory Issue Batch Excel

ในแลปนี้ เราจะยกระดับจากการวิเคราะห์ข้อมูลทีละ 1 รายการ (เหมือนใน Lab 3) ไปสู่การประมวลผลข้อมูลจำนวนมาก (Batch Processing) โดยอ่านข้อมูลจากไฟล์ JSON/Excel ส่งให้ AI วิเคราะห์ทีละบรรทัด แล้วเขียนผลลัพธ์กลับลงไปในไฟล์ Excel อัตโนมัติ

แลปนี้มีประโยชน์มากสำหรับแผนกที่มีข้อมูลดิบไหลเข้ามาเยอะ ๆ ในแต่ละวัน (เช่น ตาราง Log ปัญหาเครื่องจักร, ใบแจ้งซ่อม, รอยตำหนิชิ้นงาน) และต้องการใช้ AI เป็นตัวช่วยสรุปอัตโนมัติ

## เป้าหมายของ Lab

1. เรียนรู้วิธีใช้งาน **Pandas** พื้นฐาน (การอ่านตาราง, การวนลูป DataFrame, และการเขียนลง Excel)
2. นำฟังก์ชัน AI มาเรียกใช้แบบลูป (Loop) เพื่อประมวลผลข้อมูลหลายแถว
3. ทราบถึงวิธีแสดงผลการประมวลผลเป็นหน้าเว็บด้วย Streamlit Dataframe
4. ฝึกเพิ่ม field ใหม่ใน prompt และเขียน logic แยกกรณีตาม priority ที่ AI วิเคราะห์ออกมา (ต่อยอดจาก Lab 3)
5. เห็นตัวอย่างการนำ prompt เดียวกันไปใช้กับหลายแผนก/หัวข้อข้อมูล (Factory Issue, Purchasing, Production Planning, Safety Checklist) ผ่าน dropdown เลือกหัวข้อใน `app_streamlit.py`

## โครงสร้างไฟล์ในโฟลเดอร์นี้

- `starter.py` - สคริปต์รัน Batch Processing บน Terminal ธรรมดา ซึ่งจะอ่าน `factory_issues.json` ประมวลผล และเซฟเป็น `factory_issues_analyzed.xlsx` **มีจุดที่ต้องเติมเองอยู่ 3 จุด** (ดูหัวข้อ "กิจกรรมท้าทาย" ด้านล่าง)
- `solution.py` - สคริปต์เฉลยของจุดที่ต้องเติมเองทั้ง 3 จุดใน `starter.py`
- `app_streamlit.py` - หน้าเว็บที่เปิดให้ผู้ใช้เลือกแผนก/หัวข้อข้อมูล แล้วอัปโหลดไฟล์รายงาน (Excel/CSV) ระบบจะประมวลผลแล้วมีปุ่มให้คลิกดาวน์โหลดไฟล์ผลลัพธ์กลับไป **มี TODO 1 จุด** ให้เพิ่มคอลัมน์ Action Required แบบเดียวกับ `starter.py` (ใช้ได้เฉพาะหัวข้อ Factory Issue)

## วิธีการรัน

### รันสคริปต์ประมวลผลแบบ Terminal
```bash
python workshops/lab-04-factory-issue-batch-excel/starter.py
```
*(เมื่อรันจบ ให้ลองเปิดโฟลเดอร์เพื่อดูไฟล์ `factory_issues_analyzed.xlsx` ที่ถูกสร้างขึ้น)*

### รันผ่านหน้าเว็บ Streamlit (อัปโหลด/ดาวน์โหลดไฟล์)
```bash
streamlit run workshops/lab-04-factory-issue-batch-excel/app_streamlit.py
```
เลือกแผนก/หัวข้อข้อมูลจาก dropdown ด้านบนของหน้าเว็บก่อน แล้วอัปโหลดไฟล์ตัวอย่างที่ตรงกับหัวข้อนั้น:

| หัวข้อ (dropdown) | ไฟล์ตัวอย่างที่ใช้อัปโหลดทดสอบ |
| --- | --- |
| Factory Issue | `sample-data/factory_issues_sample.xlsx` |
| Purchasing | `sample-data/purchase_requests_sample.csv` |
| Production Planning | `sample-data/production_notes_sample.csv` |
| Safety Checklist | `sample-data/safety_checklist_notes_sample.csv` |

*(ทุกไฟล์ตัวอย่างมีคอลัมน์ชื่อ `issue_report` เป็นข้อความที่จะให้ AI วิเคราะห์ ไม่ว่าจะเป็นหัวข้อไหนก็ตาม)*

## กิจกรรมท้าทาย (Challenge)

1. **เพิ่ม field ใหม่ใน prompt:** ในฟังก์ชัน `analyze_issue` ของ `starter.py` แทนที่บรรทัด `[TODO 1: ...]` ทั้งสองบรรทัดในส่วน Rules ด้วยกฎเรื่อง `missing_information` และ `confidence` แล้วเพิ่มชื่อ field ทั้งสองต่อท้ายบรรทัด `category, priority, summary` จากนั้นดึงค่ามาใส่เป็นคอลัมน์ใหม่ `Missing_Info` และ `Confidence` ในผลลัพธ์ (ดูตัวอย่างที่ทำไว้แล้วใน `app_streamlit.py`)
2. **เขียน routing logic เอง:** เขียนฟังก์ชัน `get_action_required(priority)` ขึ้นมาเองใน `starter.py` (ยังไม่มีให้) ที่คืนค่าข้อความว่าควรทำอะไรต่อตามระดับ priority (คล้ายกับ `get_routing_action` ใน Lab 3) แล้วเติมเป็นคอลัมน์ `Action_Required` — และทำแบบเดียวกันใน `app_streamlit.py` เป็นคอลัมน์ `AI_Action_Required`
3. **ตรวจผลลัพธ์:** รันแล้วเปิดไฟล์ Excel ดูว่าคอลัมน์ `Missing_Info`, `Confidence`, `Action_Required` ที่เพิ่มเข้ามาในข้อ 1-2 แสดงถูกต้องหรือไม่ ถ้าติดขัดให้เทียบกับ `solution.py`
4. **เพิ่มข้อมูลทดสอบ:** ลองเปิดไฟล์ `sample-data/factory_issues.json` แล้วเพิ่มเคสใหม่เข้าไปอีก 2-3 เคส จากนั้นรัน `starter.py` หรืออัปโหลดไฟล์ในเว็บใหม่ เพื่อดูว่า AI สามารถประมวลผลเพิ่มได้ตามที่เราใส่ไปหรือไม่
5. **ปรับโค้ดการดาวน์โหลด:** สังเกตโค้ดใน `app_streamlit.py` ที่ใช้ `io.BytesIO()` และ `st.download_button()` นี่คือเทคนิคการเซฟไฟล์ Excel ลงบนเว็บโดยไม่ต้องสร้างไฟล์จริงบนเซิร์ฟเวอร์!
6. **ลองสลับแผนก:** เปิด `app_streamlit.py` ดู dict `PROMPT_BUILDERS` — สังเกตว่า prompt ของแต่ละแผนก (Purchasing, Production Planning, Safety Checklist) ใช้โครงสร้าง Role/Task/Context/Rules/Output Format เหมือนกันหมด (ดูหลักการได้ใน `docs/04-prompt-engineering.md`) ต่างกันแค่เนื้อหา ลองเพิ่มแผนกที่ 5 ของตัวเองเข้าไปใน dict นี้ดู แล้วทำไฟล์ sample CSV คอลัมน์ `issue_report` มาทดสอบ
