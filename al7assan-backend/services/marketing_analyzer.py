# services/marketing_analyzer.py
import pandas as pd
from sklearn.cluster import KMeans

def analyze_customers(sales_data):
    """
    sales_ قائمة: [{"customer_id", "total_spent", "frequency", "last_purchase"}]
    """
    if len(sales_data) < 2:
        return {"message": "بيانات غير كافية"}

    df = pd.DataFrame(sales_data)
    
    # تحليل العملاء (مثل: VIP، نشيط، نائم)
    X = df[['total_spent', 'frequency']]
    kmeans = KMeans(n_clusters=3, random_state=0).fit(X)
    df['cluster'] = kmeans.labels_

    segments = {
        "vip": df[df['cluster'] == 0].to_dict('records'),
        "active": df[df['cluster'] == 1].to_dict('records'),
        "dormant": df[df['cluster'] == 2].to_dict('records')
    }

    recommendations = [
        "أرسل عرض خاص للعملاء النائمين",
        "قدّم ولاءً للعملاء الـ VIP",
        "نشّط العملاء النشطين بحملة توصية"
    ]

    return {
        "customer_segments": {k: len(v) for k, v in segments.items()},
        "recommendations": recommendations
    }
