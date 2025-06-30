# 🚗 SkillAlert: Real-Time Car Painter Job Match (Pilot for Barrie)

## 💡 Use Case
Your brother is a car painter in Barrie who wants to:
- Visit car shops in person
- Show them a QR code on his phone
- Let them **easily notify him** if they need a paint job
- Start simple and grow into a platform later

This MVP allows him to:
- Share a **link or QR code** that opens a form
- The form is filled by the car shop → He gets notified instantly

---

## 🚀 What Changed
This MVP is now **specific to car painting**, uses just one input form, and works directly from a shared browser link.

---

## ✅ Quick Features
- Painter registers location & availability
- Car shop opens a simple form (via QR)
- Fills: name, car type, job details, contact info
- Painter gets email or SMS instantly

---

## 📂 Folder Structure
```bash
skillalert_mvp/
├── app.py                  # Streamlit interface for both parties
├── utils/
│   └── notifier.py         # (Email/SMS logic)
├── data/
│   └── leads.json          # Store incoming leads (for demo)
├── requirements.txt
└── README.md
```

---

## 🖼️ App Screenshot (Demo)
> “Hi, I’m a car painter. Scan this code to reach me if you ever need work done.”

---

## 📲 What to Send to the Car Shop
Use a **QR Code Generator** (like [https://qrcode-monkey.com](https://qrcode-monkey.com)) with the URL from your deployed app (e.g. Streamlit Share or ngrok URL).

The QR leads to a simple form: `Need a painter? Fill this.`

---

## ✉️ Notifier Setup (Minimal)
For now, it just **stores job leads** in `leads.json`. Email/SMS alerts can be added with:
- **Email**: [SendGrid](https://sendgrid.com/), SMTP
- **SMS**: [Twilio](https://twilio.com)

---

## ▶️ How to Run This Pilot
```bash
git clone https://github.com/your-username/skillalert_mvp.git
cd skillalert_mvp
pip install -r requirements.txt
streamlit run app.py
```

---

## 🧾 Example: Form Data from Shop
- Car type: Ford F150
- Job: Rear panel repaint
- Contact: john@autoshop.com

→ Gets saved & sent to painter.

---

## 🛠️ To Add Later
- Full booking system
- Painter calendar view
- Rating system for reliability
- Dashboard for all job types

---

## 💬 Contact & Feedback
Created as part of the HumanPlus Thesis pilot: helping communities build micro-economies through ethical AI.

Barrie – Waterloo – GTA focused.

---

## 📍 READY TO TEST
Use Streamlit Share or render with `ngrok`, then create your QR!
Let me know if you want the actual `app.py` and QR created now.
