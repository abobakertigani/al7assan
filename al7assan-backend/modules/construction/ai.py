# modules/construction/ai.py
import pandas as pd

def predict_delay(project_id, current_progress, days_left):
    if current_progress / days_left < 0.05:
        return "تحذير: خطر التأخير"
    return "على المسار الصحيح"

def optimize_resource_allocation(tasks):
    return sorted(tasks, key=lambda x: x['priority'])
