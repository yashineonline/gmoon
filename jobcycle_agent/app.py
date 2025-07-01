# jobcycle_agent/app.py

import streamlit as st
from langgraph_config import build_job_graph

st.set_page_config(page_title="JobCycle Agent", page_icon="🧠")
st.title("🧠 JobCycle AI – Find Work That Fits You")
st.markdown("Enter your experience, skills, or personal story. We'll help you match to possible job roles.")

profile_input = st.text_area("📝 Enter your profile here:", height=200)

if st.button("🚀 Match Me to Jobs"):
    graph = build_job_graph()
    state = {"profile_data": profile_input}
    result = graph.invoke(state)

    st.success("Job match complete!")
    st.subheader("📌 Extracted Skills")
    st.write(result.get("skills", []))

    st.subheader("🔍 Recommended Jobs")
    st.write(result.get("job_matches", [])[0])

