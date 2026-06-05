# Lab 4 - IT Ticket Classifier

## Goal

สร้าง Mini AI Agent ที่แยกประเภท IT Ticket และแสดงให้เห็นว่า JSON output ถูก route ไปยังทีมที่รับผิดชอบ และสร้าง first response ส่งกลับ user ได้ทันที

## Input

IT Ticket จาก user (จาก `sample-data/it_tickets.json`)

## Output Fields

| Field | ใช้ทำอะไร |
| --- | --- |
| `summary` | แสดงใน ticketing system / log |
| `category` | กำหนด routing ว่าส่งไปทีมไหน |
| `priority` | กำหนด SLA และความเร่งด่วน |
| `assigned_team` | ทีมที่ AI แนะนำให้รับผิดชอบ |
| `first_response` | ข้อความตอบกลับ user ได้ทันที |

## Routing Table

| Category | Routed To |
| --- | --- |
| Network | Network Operations (NOC) |
| Hardware | Desktop Support |
| Software | Application Support |
| Account/Login | IT Helpdesk L1 |
| ERP/System | ERP Support Team |
| Security | IT Security |
| Other | IT Helpdesk L1 |

## Output Flow

```text
sample-data/it_tickets.json  (3 tickets)
      |
      v
  Loop each ticket
      |
      v
  AI API Call  -->  JSON string
      |
  json.loads()
      |
      v
  category field  -->  TEAM_ROUTING dict  -->  assigned team
      |
  first_response field  -->  ส่งกลับ user ได้ทันที
      |
      v
  ticket_log.json  (บันทึกทุก ticket พร้อม timestamp)
      |
      v
  Routing Summary Table (แสดงผลรวมทุก ticket)
```

## Run

```bash
# Starter: classify ticket เดียว แสดง field + first response
python workshops/lab-04-it-ticket-classifier/starter.py

# Solution: batch process ทั้ง 3 ticket + routing + save log
python workshops/lab-04-it-ticket-classifier/solution.py
```

## Challenge

1. เพิ่ม ticket ใหม่ใน `sample-data/it_tickets.json` แล้วรัน solution อีกครั้ง
2. ลองเพิ่ม category ใหม่ใน `TEAM_ROUTING` เช่น `"CCTV": "Facility IT"`
3. ลองให้ AI เพิ่ม field `estimated_resolution_time` แล้วแสดงใน summary
