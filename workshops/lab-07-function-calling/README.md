# Lab 7 (Bonus) - Function Calling / Tool Use

## Goal

ให้ AI เรียกฟังก์ชัน Python (`get_supplier_status`) เพื่อดึงข้อมูล "สถานะ supplier" จาก mock database แล้วใช้ข้อมูลนั้นตอบคำถาม ตามแนวคิดใน `docs/09-function-calling.md`

## What You Will Learn

- การประกาศ `tools` (function schema) ให้ AI รู้จัก
- การอ่าน `tool_calls` จาก response และดึง argument ที่ AI เลือก
- การส่งผลลัพธ์ฟังก์ชันกลับไปด้วย role `"tool"` เพื่อให้ AI สรุปคำตอบสุดท้าย

## Mock Data

```python
SUPPLIER_DB = {
    "SUP-001": {"status": "Delayed", "eta": "2026-06-20"},
    "SUP-002": {"status": "On Time", "eta": "2026-06-15"},
    "SUP-003": {"status": "Pending Documents", "eta": "-"},
}
```

## Flow

```text
User: "สถานะของ SUP-001 ตอนนี้เป็นอย่างไร"
      |
      v
AI ตัดสินใจเรียก get_supplier_status(supplier_id="SUP-001")
      |
      v
Python รันฟังก์ชันจริง --> {"status": "Delayed", "eta": "2026-06-20"}
      |
      v
ส่งผลลัพธ์กลับไปให้ AI (role: "tool")
      |
      v
AI สรุปคำตอบสุดท้ายเป็นภาษาที่ user เข้าใจ
```

## Run

```bash
python workshops/lab-07-function-calling/starter.py
```

## Challenge

1. ลองถาม supplier_id อื่น เช่น `SUP-002`, `SUP-003` และ id ที่ไม่มีในฐานข้อมูล เช่น `SUP-999`
2. เพิ่มฟังก์ชันใหม่ `get_open_ticket_count(team: str)` พร้อม mock data แล้วเพิ่มเข้า `tools`
3. (Advanced) ลองถามคำถามที่ต้องใช้ทั้งสองฟังก์ชันในประโยคเดียว แล้วสังเกตว่า AI เลือกเรียกฟังก์ชันถูกต้องหรือไม่
