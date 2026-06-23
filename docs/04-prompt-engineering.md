# 04 - Prompt Engineering for API

## Prompt สำหรับ API ควรมีโครงสร้าง

Prompt ที่ดีควรระบุให้ชัดว่า AI ต้องรับบทบาทอะไร ทำอะไร ใช้กติกาแบบไหน และตอบกลับในรูปแบบใด

---

## Prompt Structure

```text
Role: AI ต้องรับบทบาทอะไร
Task: ต้องทำอะไร
Context: ข้อมูลประกอบคืออะไร
Rules: ข้อกำหนดหรือข้อห้าม
Output Format: ต้องตอบกลับเป็นรูปแบบใด
Input: ข้อมูลจริงที่ให้วิเคราะห์
```

---

## Template ตัวอย่าง

```text
You are an AI assistant for factory issue management at BKC.

Task:
Analyze the issue report below.

Rules:
- Do not assume missing information.
- Classify the issue as Quality, Delivery, Document, IT, Commercial, or Other.
- Set priority as Low, Medium, or High.
- Recommend the next action.

Output format:
Return JSON only with these fields:
summary, category, priority, missing_information, recommended_action

Issue report:
{issue_report}
```

---

## หลักการสำคัญ

- ระบุ output format ให้ชัด
- ถ้าต้องการ JSON ให้บอก field ที่ต้องการ
- ถ้าข้อมูลไม่ครบ ให้สั่ง AI ว่าไม่ต้องเดา
- ให้ตัวอย่าง category หรือ business rules ที่ต้องการ

---

## Model Parameters (การตั้งค่าพฤติกรรมโมเดล)

นอกจากการเขียน Prompt แล้ว การตั้งค่า **Parameters** ก่อนส่ง Request ให้ AI มีผลลัพธ์โดยตรงต่อความแม่นยำ:

- **Temperature (0.0 - 2.0):** ควบคุม "ความสร้างสรรค์"
  - หากตั้งเป็น `0.0` โมเดลจะตอบตรงไปตรงมา (Deterministic) เหมาะกับงานคัดแยกหมวดหมู่, สกัดข้อมูล และดึงผลลัพธ์แบบ JSON
  - หากตั้งเป็น `0.7` โมเดลจะมีความยืดหยุ่นสูง เหมาะกับการร่างอีเมล หรือหาไอเดียใหม่ๆ
- **Max Tokens:** ควบคุมความยาวสูงสุดของคำตอบ ช่วยให้เราจำกัดงบประมาณและป้องกัน AI ร่ายยาวเกินไป

---

## Few-Shot Prompting (การยกตัวอย่าง)

ในการทำงานจริงโรงงานมีคำศัพท์เฉพาะ (Jargon) เยอะมาก การอธิบายแค่ "กฎ (Rules)" บางครั้ง AI อาจไม่เข้าใจ การเพิ่ม **"ตัวอย่าง (Examples)"** 1-2 อันเข้าไปใน Prompt จะช่วยเพิ่มความแม่นยำได้มหาศาล

**ตัวอย่างการใส่ Few-shot ใน Prompt:**

```text
... (ส่วนของ Role, Task, Rules เหมือนเดิม) ...

Examples:
User Input: "เซ็นเซอร์ไฟหน้าจอเครื่องจักรไม่ติด"
AI Output: {"category": "Electrical", "priority": "Medium"}

User Input: "พนักงานลืมใส่แว่นตาเซฟตี้ขณะเชื่อมเหล็ก"
AI Output: {"category": "Safety/EHS", "priority": "High"}

Issue report:
{issue_report}
```
