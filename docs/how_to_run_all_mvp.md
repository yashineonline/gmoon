# 🚀 How to Run All MVPs in the Human-plus-platform

This guide walks you through running each MVP (Minimum Viable Product) inside the Human-plus-platform repo. You can copy-paste or run these commands in your terminal after cloning the repo.

---

## 🧰 Prerequisites

- Python 3.9+
- `pip` or `conda`
- Recommended: Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

---

## 📦 Install Requirements

From the root of your repo:
```bash
pip install -r requirements.txt
```

---

## 🍲 FoodCycle AI
```bash
cd foodcycle_ai
streamlit run app.py
```

---

## 🧠 JobCycle Agent
```bash
cd jobcycle_agent
pip install -r requirements.txt

# If using OpenAI:
export OPENAI_API_KEY=your_key

# If using Groq:
export GROQ_API_KEY=your_key

# If using Gemini:
export GOOGLE_API_KEY=your_key

streamlit run app.py
```

---

## 💬 EmojiTalk
```bash
cd emojitalk_mvp
streamlit run app.py
```

---

## 🏙️ CivicPulse
```bash
cd civicpulse
streamlit run app.py
```

---

## 🚗 ParkOptimizr
```bash
cd parking_optimizr
streamlit run app.py
```

---

## 🩺 MedicFind
```bash
cd medicfind
streamlit run app.py
```

---

## 🧠 CivicSolver
```bash
cd civic_solver
streamlit run app.py
```

---

## 💡 Notes
- If any subfolder has its own `requirements.txt`, you may run `pip install -r requirements.txt` inside that folder
- Make sure data files (like `.json`) are in the expected relative paths
- You can test locally first, then deploy to [Streamlit Cloud](https://streamlit.io/cloud)

---

## ✅ Done?
You can now showcase the MVPs or start improving them. Each project can evolve from MVP to full feature — feel free to fork, clone, remix, or extend!
