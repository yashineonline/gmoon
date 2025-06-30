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

def find_best_spots(user_day, prefer_free, want_dynamo, data):
    results = []
    for spot in data:
        if user_day in spot['availability'] or "Everyday" in spot['availability']:
            if prefer_free and not spot['is_free']:
                continue
            if want_dynamo and not spot['has_dynamo_unit']:
                continue
            results.append(spot)
    return sorted(results, key=lambda x: x['price_per_hour'])



