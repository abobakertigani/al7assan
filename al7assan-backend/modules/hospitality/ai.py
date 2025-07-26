# modules/hospitality/ai.py
import pandas as pd 

def predict_peak_season(month):
    peak_months = [6, 7, 8, 12]
    return "موسم الذروة" if month in peak_months else "موسم منخفض"

def recommend_pricing(occupancy_rate, base_price):
    if occupancy_rate > 80:
        return base_price * 1.3
    elif occupancy_rate < 40:
        return base_price * 0.8
    return base_price 
