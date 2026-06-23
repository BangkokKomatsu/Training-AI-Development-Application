# 07 - Prompt Engineering ขั้นสูง (Advanced)

> เนื้อหาเสริมต่อจาก `04-prompt-engineering.md` เหมาะสำหรับผู้เรียนที่ทำ Lab 2-4 เสร็จแล้วและต้องการปรับ prompt ให้แม่นยำขึ้น

---

## 1. Few-shot Examples

การให้ "ตัวอย่างคำตอบที่ถูกต้อง" ใน prompt ช่วยให้ AI ตอบในรูปแบบและน้ำเสียงที่ต้องการได้แม่นยำขึ้น โดยเฉพาะเรื่อง category หรือ priority ที่มีกฎเฉพาะขององค์กร

### ก่อนปรับ (Zero-shot)

```text
Classify the issue as Quality, Delivery, Document, IT, Commercial, or Other.
```

### หลังปรับ (Few-shot)

```text
Classify the issue as Quality, Delivery, Document, IT, Commercial, or Other.

Examples:
Input: "สินค้ามีรอยขีดข่วน ยังไม่แจ้ง lot number"
Output: {"category": "Quality", "priority": "Medium"}

Input: "ส่งของล่าช้า 3 วัน เครื่องจักรเสีย"
Output: {"category": "Delivery", "priority": "High"}

Input: "Invoice ไม่มี PO number"
Output: {"category": "Document", "priority": "Low"}
```

**ผลที่ได้:** AI เห็น pattern ของการจับคู่ input กับ category/priority ทำให้ตอบสอดคล้องกับมาตรฐานของทีมมากขึ้น

---

## 2. Chain-of-Thought (คิดเป็นขั้นตอนก่อนตอบ)

บางครั้งการให้ AI "คิดก่อนตอบ" ทำให้ผลลัพธ์สุดท้ายแม่นยำขึ้น โดยให้ AI ใส่ field เหตุผลไว้ใน JSON (แต่ field สุดท้ายยังเป็น JSON ที่ใช้งานได้)

```text
Before deciding the priority, think step by step:
1. Does this issue affect production line or shipment date?
2. Is the operator at fault or is the machine just malfunctioning?
3. Based on step 1-2, choose priority.

Return JSON only with these fields:
reasoning, summary, category, priority, missing_information, recommended_action
```

> หมายเหตุ: field `reasoning` มีไว้เพื่อ debug ตอนพัฒนา ก่อนใช้งานจริงควรเอาออกจาก output ที่ส่งให้ user เพื่อลดความยาว response และ token cost

---

## 3. ลด Hallucination (AI เดาข้อมูลที่ไม่มี)

### เทคนิคที่ใช้ได้จริง

| เทคนิค | ตัวอย่างคำสั่งใน prompt |
|---|---|
| สั่งห้ามเดาตรง ๆ | `Do not assume or invent any information that is not in the input.` |
| ให้ field สำหรับบอกว่าขาดอะไร | `List all missing information in "missing_information" field.` |
| ให้ทางเลือก "ไม่ทราบ" | `If the value cannot be determined, return "Unknown" instead of guessing.` |
| จำกัด category ให้เลือกจาก list เท่านั้น | `Choose category only from: Quality, Delivery, Document, IT, Commercial, Other.` |
| ขอ confidence score | `Add a "confidence" field: High, Medium, or Low, based on how complete the input is.` |

### ตัวอย่าง prompt ที่ลด hallucination

```text
Rules:
- Do not assume or invent information that is not in the input.
- If a value cannot be determined from the input, return "Unknown".
- Choose category only from this list: Quality, Delivery, Document, IT, Commercial, Other.
- Add a "confidence" field: High, Medium, or Low.

Return JSON only with these fields:
summary, category, priority, confidence, missing_information, recommended_action
```

---

## 4. ลองทำ (Try it during class)

ใช้ไฟล์ `workshops/lab-03-factory-issue-analyzer/starter.py` หรือ `lab-04-factory-issue-batch-excel/starter.py` ที่ทำไปแล้ว แล้วลองทำ 3 อย่างนี้:

1. เพิ่ม **few-shot examples** 2-3 ตัวอย่างใน prompt แล้วดูว่า category/priority ตรงกับที่ต้องการมากขึ้นหรือไม่
2. เพิ่ม field `confidence` (High/Medium/Low) ตามเทคนิคลด hallucination แล้ว print ออกมาดู
3. ลองใส่ข้อมูล input ที่ "ข้อมูลไม่ครบ" มาก ๆ (เช่นมีแค่ประโยคเดียว) แล้วเทียบผลลัพธ์ก่อน/หลังเพิ่ม rules ว่า AI เดาข้อมูลน้อยลงหรือไม่

> เป้าหมาย: ให้เห็นว่า prompt ที่ออกแบบดี ส่งผลต่อคุณภาพ output โดยตรง โดยไม่ต้องแก้โค้ด Python เลย
