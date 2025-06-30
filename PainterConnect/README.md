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

## 📱 How Shops Access It
- Deploy `client_app.py` via [Streamlit Cloud](https://share.streamlit.io) or `ngrok`
- Generate a QR code with the public link
- Shop scans QR → Opens form → Submits → Painter gets notified

---

## 🧪 Sample Job Request Flow
- Shop: “Repaint Toyota Camry bumper on Thursday 2pm”
- Saved to `jobs.json`
- Painter dashboard shows:
  > New job from AutoFix Ltd – Thursday 2pm
  > [Accept] or [Reschedule]

---

## 📦 requirements.txt
```
streamlit
geopy
```

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

## 🧠 Maintained by: Yashine Goolam Hossen (Waterloo, Canada)
