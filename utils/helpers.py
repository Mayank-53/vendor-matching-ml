
import pandas as pd
from sklearn.metrics.pairwise import haversine_distances
from math import radians
import json

def calculate_distance(coord1, coord2):
    coord1 = [radians(coord1[0]), radians(coord1[1])]
    coord2 = [radians(coord2[0]), radians(coord2[1])]
    result = haversine_distances([coord1, coord2])
    return result[0][1] * 6371000 / 1000  # in kilometers

def match_customer_to_technicians(customer, technicians_df, max_distance_km=50):
    matches = []
    for _, tech in technicians_df.iterrows():
        if (
            tech['city'].lower() == customer['city'].lower() and
            tech['brand'].lower() == customer['brand'].lower() and
            tech['model'].lower() == customer['model'].lower() and
            tech['available'] == 1
        ):
            dist = calculate_distance((customer['lat'], customer['lon']), (tech['lat'], tech['lon']))
            if dist <= max_distance_km:
                score = dist * 0.5 + tech['price'] * 0.5
                matches.append({
                    "id": tech['id'],
                    "name": tech['name'],
                    "distance_km": round(dist, 2),
                    "price": tech['price'],
                    "score": round(score, 2),
                    "phone": tech['phone']
                })
    matches.sort(key=lambda x: x['score'])
    return matches[:5]
