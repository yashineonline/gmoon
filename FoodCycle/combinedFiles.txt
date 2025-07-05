### foodcycle_ai/app.py
import streamlit as st
from agents.impact_calculator import calculate_savings
from agents.match_community import suggest_recipients
from utils.job_matcher import recommend_jobs

st.title("🌾 FoodCycle AI")
st.write("Match surplus food to community, calculate impact, and create local jobs.")

store_name = st.text_input("Retailer Name", "Walmart - Kitchener")
food_items = st.text_area("Surplus Food Log (e.g. 20kg bananas, 15 bread, 5 milk)")

if st.button("Generate Report"):
    savings = calculate_savings(food_items)
    recipients = suggest_recipients(food_items)
    jobs = recommend_jobs(food_items)

    st.subheader("💰 Savings Estimate")
    st.markdown(savings)

    st.subheader("🏘️ Suggested Recipients")
    st.markdown(recipients)

    st.subheader("👷‍♀️ Job/Volunteer Opportunities")
    st.markdown(jobs)


### foodcycle_ai/agents/impact_calculator.py
def calculate_savings(log: str) -> str:
    # Placeholder logic
    item_count = len(log.strip().split("\n"))
    savings_dollars = item_count * 8.5
    saved_kw = item_count * 1.2
    return f"**Approx. Savings:** ${savings_dollars:.2f}\n**Energy Saved:** {saved_kw:.1f} kWh\n**Landfill Cost Avoided:** ${item_count * 2:.2f}"


### foodcycle_ai/agents/match_community.py
def suggest_recipients(log: str) -> str:
    # Placeholder output
    return "- House of Friendship (2.1km)\n- Ray of Hope (3.0km)\n- UW Food Bank (1.5km)"


### foodcycle_ai/utils/job_matcher.py
def recommend_jobs(log: str) -> str:
    # Placeholder job mapping
    return ("- Hire a driver (1hr/day)\n"
            "- Volunteer coordinator (3hr/week)\n"
            "- Student intern: Data/impact reporting\n")


### foodcycle_ai/requirements.txt
streamlit


### foodcycle_ai/README.md
# FoodCycle AI: Surplus Food → Community → Jobs

A scalable MVP designed to:
- Match surplus food with local community recipients
- Estimate economic & energy savings
- Suggest micro-employment and volunteer opportunities

## 🔁 Workflow
1. Input surplus food list
2. AI suggests local recipients and calculates savings
3. Recommends micro-jobs to manage donation

## 🚀 How to Run
```bash
pip install -r requirements.txt
streamlit run app.py
```

## 🏙️ Pilot Use Case: Waterloo, ON
- Stores: Walmart, Zehrs, FreshCo
- Recipients: Shelters, campus food banks
- Jobs: Delivery drivers, coordinators, student analysts

## 🧠 Expansion Ideas
- Real-time maps + routing
- App store + web interface
- AI-powered PR & donation impact reporting
- QR codes on receipts for citizen tracking
