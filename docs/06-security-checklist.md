# 06 - Security Checklist

## API Key Safety

- ใช้ `.env` เพื่อเก็บ API Key
- เพิ่ม `.env` ใน `.gitignore`
- ห้าม hard-code key ใน Python file
- หาก key หลุด ให้แจ้งผู้ดูแลทันที
- หลังอบรมควร rotate หรือ revoke key ที่ใช้ร่วมกัน

---

## Data Privacy

ห้ามใช้ข้อมูลเหล่านี้ใน workshop:

- Customer data
- Personal data
- Contract
- ราคา
- ข้อมูลทางการเงิน
- ข้อมูล supplier จริงที่เป็นความลับ
- เอกสารภายในที่ไม่ได้รับอนุญาต

---

## Human Review

AI output ต้องมีคนตรวจสอบก่อนใช้งานจริง โดยเฉพาะกรณี:

- ส่ง email ให้ supplier
- ตัดสินใจเรื่อง quality issue
- สรุปข้อมูลจากเอกสารสำคัญ
- ให้คำแนะนำเชิง business decision

---

## Prototype Limitation

Mini AI Agent ในคอร์สนี้เป็น prototype เพื่อการเรียนรู้ ยังไม่ใช่ production system
