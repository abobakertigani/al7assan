# modules/trading/ai.py
import pandas as pd 

def predict_demand(product_id, season_factor=1.0):
    base_demand = 100
    return base_demand * season_factor

def recommend_reorder(product_id, current_stock):
    if current_stock < 15:
        return "توصية: طلب إعادة تعبئة"
    return "المخزون كافٍ"
