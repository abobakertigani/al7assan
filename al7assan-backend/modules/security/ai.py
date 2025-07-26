# modules/security/ai.py
import pandas as pd 

def classify_threat_level(event_type: str, location: str):
    high_risk_areas = ["main_gate", "server_room"]
    if event_type == "intrusion" and location in high_risk_areas:
        return "critical"
    return "medium"

def recommend_response(threat_level):
    if threat_level == "critical":
        return "إرسال فرقة أمن فورًا"
    return "مراقبة مستمرة" 
