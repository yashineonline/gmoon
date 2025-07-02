import streamlit as st
import requests

st.title("📱 AppGen QA Agent")

st.markdown("Upload your mobile code (.zip) or paste code to analyze for store readiness")

code_input = st.text_area("Paste Code Here", height=200)
uploaded_file = st.file_uploader("Or Upload a .zip file")

if st.button("Analyze"):
    if code_input:
        response = requests.post("http://localhost:8000/analyze_code", data={"code": code_input})
    elif uploaded_file:
        files = {"file": (uploaded_file.name, uploaded_file.read())}
        response = requests.post("http://localhost:8000/analyze_code", files=files)
    else:
        st.warning("Please provide code or upload a file.")
        st.stop()

    if response.status_code == 200:
        st.markdown("### 📋 QA Report:")
        st.code(response.json()["report"])
    else:
        st.error("Error analyzing the code. Please check the input.")
