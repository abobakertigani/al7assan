# services/quality_analyzer.py
def analyze_defects(defect_records):
    """
    defect_records: [{"product", "defect_type", "quantity", "date"}]
    """
    from collections import Counter
    defect_types = Counter([d["defect_type"] for d in defect_records])
    
    top_defect = defect_types.most_common(1)[0] if defect_types else None
    
    return {
        "total_defects": sum(defect_types.values()),
        "top_issue": top_defect[0] if top_defect else "لا يوجد",
        "recommendation": f"مراجعة عملية التصنيع لـ {top_defect[0]}" if top_defect else "لا توجد مشكلات"
    }
