# 01 - Microsoft Foundry Concept

## Microsoft Foundry คืออะไรในบริบทของคอร์สนี้

ในคอร์สนี้ Microsoft Foundry คือพื้นที่ที่ BKC ใช้สำหรับเตรียม AI Model, Deployment, Endpoint และ API Key ให้ผู้เรียนเรียกใช้งานผ่าน Python

ผู้เรียนไม่จำเป็นต้องสร้าง project เองทั้งหมด แต่ควรเข้าใจองค์ประกอบหลักที่ใช้ใน workshop

---

## คำศัพท์สำคัญ

| คำ | ความหมายแบบง่าย |
|---|---|
| Project | พื้นที่ทำงานใน Foundry |
| Model | AI model ที่ใช้ประมวลผลข้อความ |
| Deployment | การนำ model มาเปิดให้เรียกใช้งาน |
| Endpoint | URL ที่โปรแกรมส่ง request ไปหา AI |
| API Key | รหัสลับสำหรับยืนยันสิทธิ์ในการเรียก API |
| API Version | เวอร์ชันของ API ที่ endpoint รองรับ |

---

## สิ่งที่ผู้สอนต้องเตรียม

- Foundry Project
- Model Deployment
- Endpoint URL
- API Key สำหรับ workshop
- Deployment Name
- API Version
- Sample Data

---

## สิ่งที่ผู้เรียนจะได้รับจากผู้สอน

```text
AZURE_OPENAI_API_KEY=...
AZURE_OPENAI_ENDPOINT=...
AZURE_OPENAI_DEPLOYMENT=...
AZURE_OPENAI_API_VERSION=...
```

ค่าทั้งหมดนี้จะถูกใส่ในไฟล์ `.env` บนเครื่องผู้เรียน และไม่ควรถูกแชร์หรือ commit ขึ้น GitHub
