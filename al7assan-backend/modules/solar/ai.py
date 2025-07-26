# modules/solar/ai.py
import pandas as pd
def predict_energy(date, irradiance, temperature):
    """
    تنبؤ بالإنتاج بناءً على الطقس
    """
    return irradiance * 0.18 * (1 - 0.005 * (temperature - 25))

def recommend_cleaning(last_cleaned_date):
    days = (datetime.now() - last_cleaned_date).days
    return "قم بالتنظيف" if days > 30 else "لا حاجة للتنظيف"
