### HumanPlus-Platform/parking_optimizr/app.py
import streamlit as st
import json
from utils.match_logic import find_nearby_spots

# Load sample data
with open("parking_optimizr/data/sample_parking_spots.json", "r") as f:
    parking_data = json.load(f)

st.set_page_config(page_title="ParkOptimizr", layout="centered")
st.title("🚗 ParkOptimizr - Smarter Parking, Greener Cities")

user_lat = st.number_input("Enter your latitude:", format="%.6f")
user_lon = st.number_input("Enter your longitude:", format="%.6f")
max_distance = st.slider("Max walking distance (km):", 0.1, 5.0, 1.0)

if st.button("Find Parking"):
    results = find_nearby_spots(user_lat, user_lon, parking_data, max_distance)
    if results:
        st.success(f"Found {len(results)} nearby parking spots:")
        for r in results:
            st.write(f"🏢 {r['name']} — {r['distance']:.2f} km — Fee: {r['fee']}")
    else:
        st.warning("No nearby parking spots found within the selected distance.")

