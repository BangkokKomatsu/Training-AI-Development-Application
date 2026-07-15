# Lab 2 - Prompt to JSON

## Goal

ฝึกเขียน Prompt ให้ AI ตอบกลับเป็น JSON และเรียนรู้การนำ JSON นั้นไปใช้ต่อในระบบงานได้จริง

## What You Will Learn

- Prompt structure
- Output format control
- JSON response และการ parse ด้วย `json.loads()`
- การสั่งให้ AI ไม่เดาข้อมูลที่ไม่มี
- นำ field จาก JSON ไปใช้ใน logic ต่อ (routing, saving, display)

## Output Flow

```text
Issue Report (text)
      |
      v
  AI API Call
      |
      v
  JSON string  <-- raw output จาก AI
      |
  json.loads()
      |
      v
  Python dict  <-- เข้าถึง field ได้
      |
      +-- result["priority"] --> routing decision
      |
      +-- result["summary"]  --> display / log
      |
      v
  lab02_output.json  <-- ส่งต่อระบบอื่น เช่น ERP, dashboard
```

## Run

```bash
python workshops/lab-02-prompt-to-json/starter.py
```

## Challenge

1. ในไฟล์ `starter.py` หลังบรรทัด `print(raw_output)` ให้เขียนโค้ดเพิ่มเอง:
   - `result = json.loads(raw_output)` เพื่อแปลง JSON string เป็น Python dict
   - `print(result["priority"])` และ `print(result["recommended_action"])` เพื่อดึง field ออกมาดู
2. เขียน logic เพิ่มตาม priority เช่น

   ```python
   if result["priority"] == "High":
       print("แจ้ง Supervisor ทันที")
   ```

3. ลองเปลี่ยน `issue_report` แล้วดูว่า priority และ category เปลี่ยนอย่างไร
4. ดู `solution.py` เพื่อเห็นว่า JSON ไป routing และบันทึกลงไฟล์อย่างไร
