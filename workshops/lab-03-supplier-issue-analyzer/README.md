# Lab 3 - Supplier Issue Analyzer

## Goal

สร้าง Mini AI Agent Prototype ที่วิเคราะห์ปัญหา Supplier และแสดงให้เห็นว่า JSON output ถูกนำไปใช้งานจริงอย่างไร ตั้งแต่ routing ตาม priority จนถึงการ draft email reply

## Input

ข้อความแจ้งปัญหาจาก Supplier (จาก `sample-data/supplier_issues.json`)

## Output Fields

| Field | ใช้ทำอะไร |
| --- | --- |
| `summary` | แสดงใน dashboard / log |
| `category` | จัดกลุ่มปัญหา (Quality, Delivery, Document...) |
| `priority` | ตัดสินใจ routing — High escalate, Medium ERP ticket, Low log |
| `missing_information` | แจ้ง supplier ว่าต้องส่งข้อมูลอะไรเพิ่ม |
| `recommended_action` | แนะนำขั้นตอนถัดไปสำหรับทีม Procurement |
| `email_reply` | Draft email พร้อม copy and paste ส่งกลับ supplier ได้เลย |

## Output Flow

```text
sample-data/supplier_issues.json  (3 cases)
      |
      v
  Loop each case
      |
      v
  AI API Call  -->  JSON string
      |
  json.loads()
      |
      v
  priority field  -->  Routing Decision
                        High   --> แจ้ง Procurement Manager ทันที
                        Medium --> สร้าง Ticket ใน ERP
                        Low    --> บันทึกใน Log
      |
  email_reply field  -->  Email Draft (copy & send)
      |
      v
  supplier_issues_output.json  (บันทึกทุก case พร้อมส่งต่อระบบ)
      |
      v
  Batch Summary (High / Medium / Low count)
```

## Run

```bash
# Starter: analyze เคสเดียว แสดงผล field + email draft
python workshops/lab-03-supplier-issue-analyzer/starter.py

# Solution: batch process ทั้ง 3 เคส + routing + save log
python workshops/lab-03-supplier-issue-analyzer/solution.py
```

## Challenge

1. เปลี่ยน `issue_report` ใน starter แล้วดูว่า category, priority และ email_reply เปลี่ยนอย่างไร
2. เพิ่มเคสใหม่ใน `sample-data/supplier_issues.json` แล้วรัน solution อีกครั้ง
3. ลองเพิ่ม field `escalation_contact` ใน prompt แล้วใช้มันใน routing logic
