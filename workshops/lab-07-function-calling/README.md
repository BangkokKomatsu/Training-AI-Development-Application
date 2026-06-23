# Lab 7 (Bonus) - Function Calling / Tool Use

## Goal

ให้ AI เรียกฟังก์ชัน Python (`get_machine_status`) เพื่อดึงข้อมูล "สถานะเครื่องจักร" จาก mock database แล้วใช้ข้อมูลนั้นตอบคำถาม ตามแนวคิดใน `docs/09-function-calling.md`

## What You Will Learn

- การประกาศ `tools` (function schema) ให้ AI รู้จัก
- การอ่าน `tool_calls` จาก response และดึง argument ที่ AI เลือก
- การส่งผลลัพธ์ฟังก์ชันกลับไปด้วย role `"tool"` เพื่อให้ AI สรุปคำตอบสุดท้าย

## Mock Data

```python
MACHINE_DB = {
    "MAC-001": {"status": "Overheating", "temperature_celsius": 85},
    "MAC-002": {"status": "Running", "temperature_celsius": 45},
    "MAC-003": {"status": "Stopped", "temperature_celsius": 25},
}
```

## Flow

```text
User: "สถานะของเครื่อง MAC-001 ตอนนี้เป็นอย่างไร อุณหภูมิเท่าไหร่"
      |
      v
AI ตัดสินใจเรียก get_machine_status(machine_id="MAC-001")
      |
      v
Python รันฟังก์ชันจริง --> {"status": "Overheating", "temperature_celsius": 85}
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

1. ลองถาม machine_id อื่น เช่น `MAC-002`, `MAC-003` และ id ที่ไม่มีในฐานข้อมูล เช่น `MAC-999`
2. เพิ่มฟังก์ชันใหม่ `get_maintenance_team(machine_type: str)` พร้อม mock data แล้วเพิ่มเข้า `tools`
3. (Advanced) ลองถามคำถามที่ต้องใช้ทั้งสองฟังก์ชันในประโยคเดียว แล้วสังเกตว่า AI เลือกเรียกฟังก์ชันถูกต้องหรือไม่
