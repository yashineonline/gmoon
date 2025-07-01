### civicpulse/app.py
import streamlit as st
from utils.report_agent import generate_report

st.title("🏙️ CivicPulse: Local Policy Feedback Agent")
st.write("Give feedback on city issues — AI helps you structure it clearly.")

topic = st.selectbox("Select a topic", ["Snow & Ice", "Transit", "Roads", "Housing", "Other"])
message = st.text_area("Describe the issue", "Slippery ice near Weber Street...")

if st.button("Generate Report"):
    report = generate_report(topic, message)
    st.markdown("### 📝 Structured Report")
    st.markdown(report)


### civicpulse/utils/report_agent.py
def generate_report(topic: str, message: str) -> str:
    import openai

    prompt = f"""
    Convert the following civic concern into a structured municipal report.
    Topic: {topic}
    Issue: {message}

    Format:
    **Category:**
    **Location:**
    **Issue:**
    **Suggested Fix:**
    **Urgency:**
    **Date:**
    """

    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response['choices'][0]['message']['content']


### civicpulse/requirements.txt
streamlit
openai


### civicpulse/README.md
# CivicPulse: Local Policy Feedback Agent

A 4-hour MVP built for civic engagement and smart city reporting.

## 🎯 Purpose
Help residents of Waterloo (or any city) structure local issue feedback using AI — making it readable, scannable, and helpful for municipal review.

## ✅ Features
- Freeform message → Structured civic report
- Topics: snow, transit, housing, road safety, etc.
- Built using Python, Streamlit, and OpenAI GPT-4o

## 🚀 How to Run
```bash
pip install -r requirements.txt
streamlit run app.py
```

## 📝 Example
**Input:**
"I slipped on Weber street last 2 weeks. Ice everywhere, no signs."

**Output:**
```markdown
**Category:** Snow & Ice
**Location:** Weber Street, Waterloo
**Issue:** Repeated pedestrian slipping hazard due to uncleared ice
**Suggested Fix:** Increase frequency of de-icing or add signage
**Urgency:** Medium
**Date:** 2025-06-29
```

## 📈 Future Work
- Integration with Google Sheets
- Export as PDF or CSV
- City-wide dashboard or university version
- Multilingual support
- Offline-first PWA
