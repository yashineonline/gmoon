import streamlit as st
import json
from utils.storage import save_job

st.title("🔧 Need a Car Painter?")

name = st.text_input("Your Shop Name")
car = st.text_input("Car Make & Model")
date = st.date_input("Preferred Date")
time = st.time_input("Preferred Time")
contact = st.text_input("Your Email or Phone")

if st.button("Submit Request"):
    job = {
        "shop": name,
        "car": car,
        "date": str(date),
        "time": str(time),
        "contact": contact
    }
    save_job(job)
    st.success("🎉 Request submitted! The painter will contact you shortly.")
