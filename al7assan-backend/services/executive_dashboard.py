# services/executive_dashboard.py
def generate_daily_report(
    hr_alerts, 
    finance_prediction, 
    inventory_alerts, 
    quality_report, 
    maintenance_alert
):
    summary = {
        "date": "2025-04-05",
        "critical_issues": 0,
        "recommendations": []
    }

    if hr_alerts: 
        summary["critical_issues"] += len(hr_alerts)
        summary["recommendations"].append("تجديد عقود الموظفين")
    
    if inventory_alerts:
        summary["recommendations"].append("طلب مخزون عاجل")
    
    if maintenance_alert.get("high_risk_machines"):
        summary["recommendations"].append("جدولة صيانة وقائية")
    
    if quality_report.get("top_issue"):
        summary["recommendations"].append("مراجعة جودة المنتج")

    summary["summary"] = f"⚠️ {summary['critical_issues']} قضايا حرجة | 💡 {len(summary['recommendations'])} توصيات"

    return summary
