# 05 - VS Code + Python Setup

## Step 1: Install Tools

ผู้เรียนควรติดตั้งเครื่องมือก่อนวันอบรม

- VS Code
- Python 3.10 ขึ้นไป
- Git

---

## Step 2: Clone หรือ Download Repository

```bash
git clone <repository-url>
cd bkc-ai-application-development-guide
```

หากไม่ได้ใช้ Git สามารถ Download เป็น ZIP แล้วแตกไฟล์ได้

---

## Step 3: Create Virtual Environment

Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

macOS / Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

## Step 4: Install Packages

```bash
pip install -r requirements.txt
```

---

## Step 5: Create `.env`

Copy `.env.example` เป็น `.env`

```bash
cp .env.example .env
```

บน Windows หากใช้ File Explorer สามารถ copy file แล้ว rename ได้

กรอกค่าที่ได้รับจากผู้สอน:

```env
AZURE_OPENAI_API_KEY=...
AZURE_OPENAI_ENDPOINT=...
AZURE_OPENAI_DEPLOYMENT=...
AZURE_OPENAI_API_VERSION=...
```

---

## Step 6: Run Lab

เข้าไปที่โฟลเดอร์ Lab แล้วรันไฟล์ Python เช่น

```bash
cd workshops/lab-01-first-api-call
python starter.py
```
