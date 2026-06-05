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
You are an AI assistant for supplier issue management at BKC.

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
