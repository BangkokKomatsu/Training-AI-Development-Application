# 09 - Function Calling / Tool Use เบื้องต้น

> เนื้อหาเสริม (Bonus) — เป็นพื้นฐานก่อนต่อยอดไปสู่ Agent ที่เชื่อมระบบภายนอกได้จริง

---

## 1. ปัญหาของ Mini AI Agent ใน Lab 1-4

Lab 1-4 ทุก output มาจาก "ความรู้และข้อความที่ส่งให้ AI" เท่านั้น AI **เรียกข้อมูลจากระบบอื่นเองไม่ได้** เช่น

- เช็คสถานะเซ็นเซอร์ของเครื่องจักรล่าสุด
- เช็คว่าใบแจ้งซ่อมนี้มีอยู่ในระบบแล้วหรือยัง
- ดึงสต็อกอะไหล่ปัจจุบันจากฐานข้อมูล

**Function Calling** คือกลไกที่ทำให้ AI สามารถ "ขอให้โปรแกรมของเรา" รันฟังก์ชัน Python แล้วส่งผลลัพธ์กลับไปให้ AI ใช้ตอบต่อ

---

## 2. แนวคิดการทำงาน

```text
1. เราบอก AI ว่ามีฟังก์ชันอะไรให้ใช้บ้าง (ชื่อ, คำอธิบาย, parameter)
2. User ถามคำถาม
3. AI ตัดสินใจว่า "ต้องเรียกฟังก์ชันไหน" และ "ใช้ parameter อะไร"
4. โปรแกรม Python รันฟังก์ชันนั้นจริง ๆ (เช่น lookup ใน dict/database)
5. ส่งผลลัพธ์ของฟังก์ชันกลับไปให้ AI
6. AI สรุปคำตอบสุดท้ายให้ user โดยใช้ข้อมูลจากฟังก์ชัน
```

---

## 3. การประกาศ Tool (Function Schema)

```python
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_machine_status",
            "description": "Get the current status and temperature of a machine by machine_id",
            "parameters": {
                "type": "object",
                "properties": {
                    "machine_id": {
                        "type": "string",
                        "description": "Machine ID, e.g. MAC-001",
                    }
                },
                "required": ["machine_id"],
            },
        },
    }
]
```

---

## 4. ฟังก์ชันจริงฝั่ง Python (Mock data)

```python
MACHINE_DB = {
    "MAC-001": {"status": "Overheating", "temperature_celsius": 85},
    "MAC-002": {"status": "Normal", "temperature_celsius": 45},
}

def get_machine_status(machine_id: str) -> dict:
    return MACHINE_DB.get(machine_id, {"status": "Unknown", "temperature_celsius": "-"})
```

---

## 5. ขั้นตอนเรียก API พร้อม Tool

```python
response = client.chat.completions.create(
    model=deployment_name,
    messages=messages,
    tools=tools,
)

message = response.choices[0].message

if message.tool_calls:
    for tool_call in message.tool_calls:
        if tool_call.function.name == "get_machine_status":
            args = json.loads(tool_call.function.arguments)
            result = get_machine_status(args["machine_id"])

            # ส่งผลลัพธ์ฟังก์ชันกลับไปให้ AI สรุปคำตอบสุดท้าย
            messages.append(message)
            messages.append({
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": json.dumps(result),
            })

    final_response = client.chat.completions.create(
        model=deployment_name,
        messages=messages,
    )
    print(final_response.choices[0].message.content)
else:
    print(message.content)
```

---

## 6. จุดนี้คือ "พื้นฐาน" ก่อน Agent เต็มรูปแบบ

| สิ่งที่ทำใน Lab นี้ | สิ่งที่ Agent เต็มรูปแบบทำเพิ่ม (คอร์สถัดไป) |
|---|---|
| Mock function / dict ในไฟล์เดียว | เชื่อมต่อ database หรือ API ของระบบจริง |
| Tool เดียว ตัดสินใจครั้งเดียว | หลาย tools, เรียกหลายรอบ, วางแผนหลายขั้นตอน |
| รันบนเครื่องผู้เรียน | Deploy เป็น service ที่ทำงานต่อเนื่อง |

---

## 7. ลองทำ (Try it during class)

ไปที่ `workshops/lab-07-function-calling/`:

1. รัน `starter.py` แล้วลองถาม "สถานะของเครื่อง MAC-001 ตอนนี้เป็นอย่างไร อุณหภูมิเท่าไหร่"
2. สังเกตว่า AI เรียก `get_machine_status` ด้วย `machine_id` ที่ถูกต้องหรือไม่
3. (Challenge) ลองเพิ่มฟังก์ชันใหม่ เช่น `get_maintenance_team(machine_type: str)` พร้อม mock data แล้วเพิ่มใน `tools` ให้ AI เลือกใช้ได้ถูกต้อง
