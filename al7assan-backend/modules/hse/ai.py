# modules/hse/ai.py
import pandas as pd 

def predict_risk_level(likelihood: str, impact: str):
    matrix = {
        ("high", "high"): "critical",
        ("high", "medium"): "high",
        ("medium", "high"): "high",
    }
    return matrix.get((likelihood, impact), "low")

def recommend_training(risk_type):
    return f"تدريب على {risk_type} مطلوب خلال 7 أيام"
