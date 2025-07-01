# jobcycle_agent/README.md

---
## 🧠 Agentic Workflow (LangGraph + GPT)
This module uses LangGraph to create a multi-step agent for assigning job roles based on a user's profile.

## 🧩 Workflow Steps
Collect Profile → Accepts raw user description

Extract Skills → Uses GPT to extract skill keywords

Match Jobs → GPT suggests 3 suitable job roles with reasoning

---
### 🔧 A simple LangGraph node flow

```python
[Start]
   ↓
[Collect Profile Info]
   ↓
[LangChain Agent: Skill Extractor]
   ↓
[LangChain Agent: Job Matcher]
   ↓
[Output: Job Suggestions + Links + Score]
```

---


### 🗂️ Folder Structure

```
human-plus-platform/
├── jobcycle_agent/
│   ├── app.py     
│   ├── langgraph_config.py
│   └── agentic_workflow.py
│   └── requirements.txt
│   └── README.md
```

---



## 📍 Example Use Case

### 🚀 `app.py`
```python
from langchain.agents import initialize_agent, load_tools
from langchain.llms import OpenAI

llm = OpenAI(temperature=0)
tools = load_tools(["wikipedia", "llm-math"], llm=llm)
agent = initialize_agent(tools, llm, agent="zero-shot-react-description")

response = agent.run("What kind of job fits someone skilled in carpentry, driving, and electrical wiring?")
```

---

## Testing 
```python
from langgraph_config import build_job_graph

graph = build_job_graph()
initial_state = {
    "profile_data": "I have 5 years experience as an electrician and also did part-time carpentry and delivery driving."
}
result = graph.invoke(initial_state)
print(result)
```

---

## ▶️ How to Run
See: [docs/how_to_run_all_mvp.md](../docs/how_to_run_all_mvp.md)




---

## Full Feature Checklist for JobCycle Agent

#### 1. Build the dataset matching logic
- Implement logic to match user profiles with job datasets

#### 2. Add Firebase backend for job tracking
- Integrate Firebase to store and track job applications

#### 3. Build the resume parser into the UI
- Add a resume upload feature and parse resumes for skills and experience

📄 Code for Resume Upload (PDF → Text)
```python
import pdfplumber

uploaded_file = st.file_uploader("Upload resume (PDF)", type=["pdf"])
if uploaded_file:
    with pdfplumber.open(uploaded_file) as pdf:
        text = "\n".join(page.extract_text() for page in pdf.pages)
    st.text_area("Parsed Resume", value=text[:2000])
```


#### 4. Scoring & Ranking Job Matches
- Compare user profile skills against each job in the dataset
- Assign a score based on skill match percentage
- Rank jobs by highest score and display the top 3

#### 5. Explainability
- Use GPT to explain why each job was recommended
- Add a toggle: “Why this match?”

#### 6. Feedback Loop for Better Matches
- Let users rate the job matches (👍 / 👎)
- Store feedback in Firebase or local JSON
- Retrain or fine-tune match logic (optional future step)

#### 7. Persistent Job History (Optional Database Layer)
- Use Firebase, Supabase, or SQLite
- Save submitted profiles and matched jobs per user session

#### 8. Email or Notification
- Allow users to receive job matches via email (using SMTP or EmailJS)
- Add button: “Email My Matches”

#### 9. Mobile Responsiveness
- Ensure the UI works well on phones (Streamlit handles this reasonably)
- Add “Copy Job Match” button for sharing via text message or WhatsApp

#### 10. Admin Dashboard
- Show number of job submissions, match success rate
- Visualize common skills using bar chart or word cloud

#### 11. Authentication (optional)
- Add simple password or Firebase Auth for persistent user sessions

#### 12. Deploy Online
- Use Streamlit Community Cloud or Hugging Face Spaces
- Include public demo link in README

---


## 🗂️ Add-ons

### 🌍 Multi-language Support
```python
from langchain.tools.translate import GoogleTranslateTool
```

- Add a language switch dropdown to app.py.
- Detect input language → translate → process.

# Extra notes to merge with above

### jobcycle_agent/app.py
import streamlit as st
from agents.interview_agent import run_interview
from agents.job_matcher import match_jobs
from utils.test_generator import generate_test

st.title("👥 JobCycle Agent: Unlock Your Next Step")
st.write("AI-powered job assistant for everyone — even if you feel unemployable.")

if 'profile' not in st.session_state:
    st.session_state.profile = {}

with st.form("job_form"):
    name = st.text_input("Your Name")
    background = st.text_area("Tell us your story / experience / interests")
    time = st.selectbox("How many hours/week can you commit?", ["<5", "5-10", "10-20", "Full-time"])
    submit = st.form_submit_button("Find Jobs")

if submit:
    st.session_state.profile = {
        "name": name,
        "background": background,
        "availability": time
    }
    job_matches = match_jobs(st.session_state.profile)
    test = generate_test(job_matches)

    st.subheader("🧠 Suggested Jobs")
    st.markdown(job_matches)

    st.subheader("📋 Mini-Suitability Test")
    st.markdown(test)

    st.download_button("Download Job Plan", f"Name: {name}\nJobs:\n{job_matches}\nTest:\n{test}", "jobcycle_plan.txt")


### jobcycle_agent/agents/interview_agent.py
def run_interview():
    # Placeholder: Future conversational agent
    return "(GPT-powered interview in development)"


### jobcycle_agent/agents/job_matcher.py
def match_jobs(profile):
    bg = profile.get("background", "")
    if "drive" in bg.lower():
        return "- Local Delivery (2-4h/day)\n- Uber Helper / Package Runner"
    elif "cook" in bg.lower() or "food" in bg.lower():
        return "- Community Kitchen Assistant\n- Food Prep Volunteer"
    elif "student" in bg.lower():
        return "- Tutoring Young Learners\n- Tech Support at Senior Centre"
    else:
        return "- Street Surveyor\n- Waste Sorting + Impact Tracking\n- Food Rescue Agent"


### jobcycle_agent/utils/test_generator.py
def generate_test(jobs):
    if "Delivery" in jobs:
        return "**Task:** Draft a polite message to send to a customer if their package is delayed by 10 minutes."
    if "Tutor" in jobs:
        return "**Task:** Explain what a fraction is to a 9-year-old in 3 sentences."
    return "**Task:** Suggest 2 ways to reduce food waste at a public event."


### jobcycle_agent/requirements.txt
streamlit


### jobcycle_agent/README.md
# JobCycle Agent: GPT-Powered Job Matchmaker for Everyone

## 🌟 Mission
Help those who feel stuck or overlooked rediscover work, purpose, and potential through AI.

## 🧰 What It Does
- Simple profile form
- GPT-based job match recommendations
- Context-aware job test
- Exports "Job Plan" to share, build on, or take to an NGO/job center

## 💼 Sample Jobs Suggested
- Delivery helper
- Food bank assistant
- Teaching support
- Elder tech aid
- Street data volunteer

## 🚀 Run Locally
```bash
pip install -r requirements.txt
streamlit run app.py
```

## 🤖 Future Additions
- Full interview agent
- Location-based matching
- Integration with FoodCycle AI
- Reputation tracker + microcredentials

## ❤️ Designed For
- Refugees
- Low-income job seekers
- Students & retirees
- Anyone who thinks "I have nothing to offer"







