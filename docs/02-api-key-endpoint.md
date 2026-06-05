# 02 - API Key, Endpoint and Deployment

## API Key คืออะไร

API Key คือรหัสลับที่ใช้ยืนยันว่าโปรแกรมของเรามีสิทธิ์เรียกใช้งาน AI Model ผ่าน Microsoft Foundry

ให้จำง่าย ๆ ว่า:

```text
API Key = บัตรผ่านสำหรับเรียก AI API
Endpoint = ประตูทางเข้า AI Service
Deployment = Model ที่ถูกเปิดให้ใช้งาน
Prompt = คำสั่งที่ส่งให้ AI
Response = คำตอบที่ AI ส่งกลับมา
```

---

## ตัวอย่างค่าที่ใช้ใน `.env`

```env
AZURE_OPENAI_API_KEY=replace_with_your_api_key
AZURE_OPENAI_ENDPOINT=https://example.openai.azure.com/
AZURE_OPENAI_DEPLOYMENT=gpt-xxx-deployment
AZURE_OPENAI_API_VERSION=api_version_from_instructor
```

---

## ทำไมต้องใช้ `.env`

ไม่ควรเขียน API Key ลงใน code โดยตรง เช่น

```python
api_key = "my-secret-key"
```

ควรเก็บไว้ใน `.env` แล้วให้ Python อ่านค่าจาก environment แทน

---

## สิ่งที่ห้ามทำ

- ห้ามส่ง API Key ใน Line group
- ห้ามแปะ API Key ใน slide
- ห้าม commit `.env` ขึ้น GitHub
- ห้ามใช้ข้อมูลจริงที่เป็นความลับในการทดสอบ
- ห้ามใช้ key ที่ไม่ใช่ของ workshop โดยไม่ได้รับอนุญาต
