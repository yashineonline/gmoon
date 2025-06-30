### parking_optimizr/README.md
# 🚗 ParkOptimizr: Smart, Shared, Sustainable

## 💡 The Problem
In cities like Waterloo, parking is:
- Expensive for residents
- Underutilized in private/commercial lots
- Environmentally wasteful (battery waste, idle cars)

## 🌟 What This MVP Solves
- Matches underused parking spots to local drivers
- Incentivizes cheap/free parking with energy-generation add-ons (like bike dynamos)
- Offers local owners micro-revenue streams for opening their unused spots
- Integrates basic electric vehicle (EV) service support
- Links shared car pools, bike drop-off, or eco-contribution incentives

---

## 🧠 Core Features
- Driver requests parking
- App finds available low-cost or green-incentive-based spots nearby
- Shows if free, paid (low), or green-offset (energy-generating) options are available
- Collects preferences: price, distance, willingness to pedal/cycle for offset
- Tracks points/credits if driver uses cycle/dynamo setup

---

## 🧪 MVP Tech Plan
- **Frontend**: Streamlit for now, upgradeable to Vue.js or React Native
- **Backend**: Python + SQLite / Firebase
- **Map**: Leaflet.js or OpenStreetMap via Streamlit plugin
- **Matching logic**: Preference + availability + incentive ranking

---

## 🛠️ MVP Implementation

### 🗂️ Folder Structure
```
parking_optimizr/
├── app.py
├── data/
│   └── sample_parking_spots.json
├── utils/
│   └── match_logic.py
├── requirements.txt
└── README.md
```

### 🔧 `requirements.txt`
```
streamlit
geopy
pandas
```

### 📍 `data/sample_parking_spots.json`
```json
[
  {
    "id": 1,
    "address": "123 King St W",
    "price_per_hour": 1,
    "is_free": false,
    "has_dynamo_unit": true,
    "availability": ["Monday", "Wednesday", "Saturday"]
  },
  {
    "id": 2,
    "address": "456 Queen St",
    "price_per_hour": 0,
    "is_free": true,
    "has_dynamo_unit": false,
    "availability": ["Everyday"]
  }
]
```

### 🧠 `utils/match_logic.py`
```python
def find_best_spots(user_day, prefer_free, want_dynamo, data):
    results = []
    for spot in data:
        if user_day in spot['availability'] or "Everyday" in spot['availability']:
            if prefer_free and not spot['is_free']:
                continue
            if want_dynamo and not spot['has_dynamo_unit']:
                continue
            results.append(spot)
    return sorted(results, key=lambda x: x['price_per_hour'])
```

### 🚀 `app.py`
```python
import streamlit as st
import json
from utils.match_logic import find_best_spots

st.title("🚗 ParkOptimizr")

# Load data
with open("data/sample_parking_spots.json") as f:
    data = json.load(f)

st.sidebar.header("Preferences")
day = st.sidebar.selectbox("Day of Parking", ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])
prefer_free = st.sidebar.checkbox("Prefer Free Spots")
want_dynamo = st.sidebar.checkbox("Willing to pedal for energy credit")

results = find_best_spots(day, prefer_free, want_dynamo, data)

st.subheader("Available Spots")
for r in results:
    st.markdown(f"**{r['address']}** - ${r['price_per_hour']} per hour")
    if r['has_dynamo_unit']:
        st.text("Includes Dynamo Unit! ⚡")
    if r['is_free']:
        st.text("Free Parking ✅")
```

---

## 📍 Example Use Case
> Yashine lives near Uptown Waterloo. Street parking is $7/hr. There's a nearby closed restaurant lot, usually empty. A part-time student uploads that she will rent her driveway for $1/hr. Another community user donates a back-lane spot with a pedal-bike energy unit. Yashine books the latter, cycles for 15 minutes, earns a credit, and stores 0.02kWh. His electric scooter is recharged by the stored energy.

---

## 🤝 Who Gains
- Landowners with unused space
- Electric car/scooter/bike users
- People who want to save money
- The environment (battery recapture & cleaner idle zones)
- City planners (traffic + emissions data)

---

## 📫 Contact & Contribute
Join the HumanPlus platform and help optimize urban life.

