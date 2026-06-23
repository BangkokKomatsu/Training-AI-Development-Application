# 03 - Token Basics

## Token คืออะไร

Token คือหน่วยย่อยของข้อความที่ AI ใช้ในการประมวลผล ทั้งข้อความที่เราส่งเข้าไปและคำตอบที่ AI สร้างกลับมา

```text
Input Tokens + Output Tokens = Total Usage
```

---

## ทำไมต้องเข้าใจ Token

Token มีผลต่อ:

- ค่าใช้จ่าย
- ความเร็วในการตอบ
- ข้อจำกัดความยาวของข้อมูลที่ส่งเข้า model
- การออกแบบ prompt ให้กระชับและชัดเจน

---

## ตัวอย่าง

Prompt สั้น:

```text
Summarize this issue.
```

Prompt ที่ดีขึ้น:

```text
Summarize this factory issue in 3 bullet points. Include problem, impact, missing information, and next action.
```

Prompt ที่ยาวขึ้นอาจให้ผลลัพธ์ดีขึ้น แต่ใช้ token มากขึ้น ผู้เรียนควรฝึกเขียน prompt ให้สมดุลระหว่างความชัดเจนและความกระชับ
