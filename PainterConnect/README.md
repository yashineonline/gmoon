### painterconnect/README.md
# 🎨 PainterConnect MVP (Phase 1)

> Real-time painter availability + shop request sync system for your brother in Barrie, Canada

---

## 🔧 MVP Overview
A two-app system:

### 1. **Painter Dashboard** (`painter_app.py`)
- Displays incoming job requests
- Allows setting availability
- Accept/reschedule functionality

### 2. **Client Request Form** (`client_app.py`)
- Car shops scan QR code to open form
- Submit paint job request with preferred time
- Saves to shared backend

---

## 🗂️ Folder Structure
```
painterconnect/
├── painter_app.py
├── client_app.py
├── utils/
│   ├── schedule.py       # painter availability & conflict check
│   └── storage.py        # load/save requests to JSON or Firebase
├── data/
│   └── jobs.json         # temporary storage for requests
├── requirements.txt
└── README.md
```

---

## 📄 client_app.py
```python
import streamlit as st
import json
from utils.storage import save_job

st.title("🔧 Need a Car Painter?")

name = st.text_input("Your Shop Name")
car = st.text_input("Car Make & Model")
date = st.date_input("Preferred Date")
time = st.time_input("Preferred Time")
contact = st.text_input("Your Email or Phone")

if st.button("Submit Request"):
    job = {
        "shop": name,
        "car": car,
        "date": str(date),
        "time": str(time),
        "contact": contact
    }
    save_job(job)
    st.success("🎉 Request submitted! The painter will contact you shortly.")
```

---

## 📄 painter_app.py
```python
import streamlit as st
from utils.storage import load_jobs

st.title("🎨 Painter Dashboard")
st.subheader("Incoming Job Requests")

jobs = load_jobs()

if not jobs:
    st.info("No new requests yet.")
else:
    for i, job in enumerate(jobs):
        with st.expander(f"Job #{i+1} - {job['shop']}"):
            st.write(f"Car: {job['car']}")
            st.write(f"Date: {job['date']}")
            st.write(f"Time: {job['time']}")
            st.write(f"Contact: {job['contact']}")
            st.button("Accept", key=f"accept_{i}")
```

---

## 📄 utils/storage.py
```python
import json
import os

DATA_PATH = "data/jobs.json"

def load_jobs():
    if not os.path.exists(DATA_PATH):
        return []
    with open(DATA_PATH, 'r') as f:
        return json.load(f)

def save_job(job):
    jobs = load_jobs()
    jobs.append(job)
    with open(DATA_PATH, 'w') as f:
        json.dump(jobs, f, indent=2)
```

---

## 📄 data/jobs.json
```json
[]
```

---

## 📦 requirements.txt
```
streamlit
```

---


## ⚙️ How to Run Locally
```bash
git clone https://github.com/your-username/PainterConnect-MVP.git
cd PainterConnect-MVP
pip install -r requirements.txt

# In terminal tab 1
streamlit run painter_app.py

# In terminal tab 2
streamlit run client_app.py
```

---

## 📦 requirements.txt
```
streamlit
geopy
```

---

## 🧪 Sample Job Request Flow
- Shop: “Repaint Toyota Camry bumper on Thursday 2pm”
- Saved to `jobs.json`
- Painter dashboard shows:
  > New job from AutoFix Ltd – Thursday 2pm
  > [Accept] or [Reschedule]

---


## 📱 How Shops Access It
- Deploy `client_app.py` via [Streamlit Cloud](https://share.streamlit.io) or `ngrok`
- Generate a QR code with the public link
- Shop scans QR → Opens form → Submits → Painter gets notified

---

## 📱 How Shops Access It
- Deploy `client_app.py` via [Streamlit Cloud](https://share.streamlit.io) or `ngrok`
- Generate a QR code with the public link
- Shop scans QR → Opens form → Submits → Painter gets notified

---

## 📍 Roadmap
- Add Google Calendar sync
- SMS/email alerts via Twilio or SendGrid
- Convert to mobile-first PWA using Next.js or FlutterFlow

---

## 🤝 Contribute
This project is part of the HumanPlus Thesis: building tools for local economy, powered by open AI + real human need.

---

## 🔐 Privacy
All job requests stay private. Add your own Firebase config or use local-only mode.

---

🧠 Maintained by: Hazmatally (Waterloo, Canada)
🧠 Concept from: Aman (Barrie, Canada)

