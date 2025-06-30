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
