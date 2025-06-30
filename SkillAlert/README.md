# 🎨 SkillAlert: Real-Time Trades & Microjob Matching

## 💡 Problem
Local tradespeople (painters, electricians, handymen, etc.) miss job opportunities because:
- They don’t have real-time access to requests from businesses
- They can’t cover vast regions efficiently
- Scheduling clashes and manual outreach take too long

## 🚀 Solution
SkillAlert connects local service providers with businesses needing on-demand help in real-time — with geolocation, availability sync, and notification triggers.

---

## 🔧 MVP Features

- 🧭 Radius-based job matching (e.g., "within 25km of Barrie")
- 📅 Painter sets availability, working hours, and travel radius
- 🛠️ Business posts job (e.g., "Need painter for store at 5pm tomorrow in Vaughan")
- 🤖 GPT classifies request, summarizes it
- 🔔 Painter gets instant alert (email/SMS/notification)
- 📆 Schedule auto-updates to prevent clashes
- ✅ Optional: Accept/Reject button in message

---

## 📚 Tech Stack
- **Frontend**: Streamlit (or Next.js for mobile-ready)
- **Backend**: Firebase / Supabase (real-time DB + auth)
- **Notifications**: Twilio (SMS), SendGrid (Email), Firebase Cloud Messaging (Push)
- **Geolocation**: Google Maps API or OpenStreetMap
- **LLM Integration**: GPT-4o for request understanding + agent-style negotiation

---

## 📦 Folder Structure
```bash
skillalert_mvp/
├── app.py                # Streamlit frontend
├── scheduler.py          # Logic to check availability
├── utils/
│   ├── notifier.py       # Sends alerts
│   └── geo_filter.py     # Distance and region matching
├── data/
│   └── mock_jobs.json    # Sample painting jobs
├── requirements.txt
└── README.md
```

---

## 📍 Example Use Case
> John, a painter in Barrie, sets radius to 30km and adds availability Mon–Fri, 9–5. A small café in Vaughan posts: "Need interior repainting on Wednesday 11am." GPT classifies it, system matches geo, no clash found → John gets SMS: "🎨 Job match in Vaughan! Interior repainting 11am Wed. Accept?"

---

## 🤝 Expansion Ideas
- Add map view of jobs nearby
- Integrate Stripe for payment + invoicing
- Support other trades (carpenters, gardeners, tutors, musicians)
- Create co-op style freelancer network by city

---

## 🌐 Relevance to HumanPlus Platform
- Adds to **JobCycle Agent** ecosystem
- Helps solve underemployment + visibility for blue-collar trades
- Encourages **local resilience** and economy building
- 100% scalable to rural, urban, or refugee community zones


---

## ▶️ How to Run
```bash
cd skillalert_mvp
pip install -r requirements.txt
streamlit run app.py
```

---

## 🗂️ Files to Create

### `app.py`
```python
import streamlit as st
import json
from utils.geo_filter import is_within_radius
from scheduler import is_available

st.set_page_config(page_title="SkillAlert", layout="centered")
st.title("🎨 SkillAlert – Painter Job Match")

lat = st.number_input("Enter your latitude:", value=44.389355)
lon = st.number_input("Enter your longitude:", value=-79.690331)
travel_radius = st.slider("Max distance (km):", 1, 50, 25)
avail_day = st.selectbox("Available Day:", ["Mon", "Tue", "Wed", "Thu", "Fri"])
avail_hour = st.slider("Available Hour:", 0, 23, 9)

if st.button("Find Matching Jobs"):
    with open("data/mock_jobs.json") as f:
        jobs = json.load(f)
    matched = []
    for job in jobs:
        if is_within_radius(lat, lon, job['lat'], job['lon'], travel_radius):
            if is_available(avail_day, avail_hour, job['day'], job['hour']):
                matched.append(job)
    if matched:
        st.success(f"Found {len(matched)} matching job(s):")
        for m in matched:
            st.write(f"📍 {m['desc']} at {m['lat']},{m['lon']} on {m['day']} at {m['hour']}:00")
    else:
        st.warning("No matches found for your location and time.")
```

### `scheduler.py`
```python
def is_available(user_day, user_hour, job_day, job_hour):
    return user_day == job_day and abs(user_hour - job_hour) <= 2
```

### `utils/geo_filter.py`
```python
from geopy.distance import geodesic

def is_within_radius(lat1, lon1, lat2, lon2, max_km):
    return geodesic((lat1, lon1), (lat2, lon2)).km <= max_km
```

### `utils/notifier.py`
```python
# Stub function – replace with actual SMS/email API later
def send_alert(to, message):
    print(f"Sending to {to}: {message}")
```

### `data/mock_jobs.json`
```json
[
  {"desc": "Paint café interior", "lat": 43.833, "lon": -79.527, "day": "Wed", "hour": 11},
  {"desc": "Garage repaint", "lat": 44.1, "lon": -79.6, "day": "Tue", "hour": 14}
]
```

### `requirements.txt`
```
streamlit
geopy
```





