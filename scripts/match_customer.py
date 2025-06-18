
import pandas as pd
import json
from utils.helpers import match_customer_to_technicians

# Load technician data
tech_df = pd.read_csv("data/technicians.csv")

# Simulated customer input
customer_query = {
    'lat': 28.6139,
    'lon': 77.2090,
    'city': 'Delhi',
    'brand': 'Samsung',
    'model': 'TV'
}

matches = match_customer_to_technicians(customer_query, tech_df)

print(json.dumps({"matches": matches}, indent=4))
