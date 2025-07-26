# modules/aquaculture/ai.py
import pandas as pd
from datetime import datetime, timedelta

def predict_harvest_date(avg_growth_rate, current_weight, target_weight):
    """
    تنبؤ بتاريخ الحصاد
    """
    days_needed = (target_weight - current_weight) / avg_growth_rate
    return (datetime.now() + timedelta(days=days_needed)).strftime("%Y-%m-%d")

def optimize_feed_schedule(species, water_temp):
    """
    اقتراح جدول التغذية
    """
    if species == "tilapia" and 28 <= water_temp <= 30:
        return "قم بالتغذية 3 مرات يوميًا، 2% من وزن الأسماك"
    elif species == "broiler":
        return "اتبع خطة التغذية: يوم 1-10: Starter، 11-24: Grower"
    return "لا توجد توصية فورية"
