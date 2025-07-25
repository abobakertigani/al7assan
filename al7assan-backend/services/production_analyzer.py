def predict_maintenance(failure_records):
    """
    failure_records: [{"date": "...", "machine": "...", "type": "..."}]
    """
    # تحليل تكرار الأعطال
    from collections import Counter
    machine_failures = Counter([f["machine"] for f in failure_records])
    
    high_risk = [machine for machine, count in machine_failures.items() if count > 3]
    
    return {
        "high_risk_machines": high_risk,
        "recommendation": "جدولة صيانة وقائية"
    }
