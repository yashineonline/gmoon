### HumanPlus-Platform/parking_optimizr/app.py
import streamlit as st
import json
from utils.match_logic import find_nearby_spots

# Load sample data
with open("data/sample_parking_spots.json", "r") as f:
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

### HumanPlus-Platform/parking_optimizr/utils/match_logic.py
from geopy.distance import geodesic

def find_nearby_spots(user_lat, user_lon, data, max_km=1.0):
    results = []
    for spot in data:
        dist = geodesic((user_lat, user_lon), (spot['lat'], spot['lon'])).km
        if dist <= max_km:
            results.append({"name": spot['name'], "fee": spot['fee'], "distance": dist})
    results.sort(key=lambda x: x["distance"])
    return results

### HumanPlus-Platform/parking_optimizr/data/sample_parking_spots.json
[
  {"name": "GreenLot A", "lat": 43.4643, "lon": -80.5204, "fee": "$3/hr"},
  {"name": "Solar Park B", "lat": 43.4650, "lon": -80.5182, "fee": "$2/hr"},
  {"name": "FreeCycle Garage", "lat": 43.4665, "lon": -80.5210, "fee": "Free with pedal energy"},
  {"name": "EV Share Spot", "lat": 43.4630, "lon": -80.5195, "fee": "$1/hr"}
]
