# modules/logistics/ai.py
import pandas as pd 
from datetime import timedelta

def optimize_route(stops):
    return sorted(stops, key=lambda x: x['priority'], reverse=True)

def predict_delivery_time(distance_km, traffic_factor=1.0):
    base_hours = distance_km / 60
    return base_hours * traffic_factor 
