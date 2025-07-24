# services/data_analyzer.py
import pandas as pd

def analyze_sales_trend(sales_data):
    """
    sales_ قائمة من الشكل [{'date': '2025-04-01', 'amount': 5000}, ...]
    """
    df = pd.DataFrame(sales_data)
    df['date'] = pd.to_datetime(df['date'])
    df.set_index('date', inplace=True)
    
    # تحليل بسيط
    total = df['amount'].sum()
    avg = df['amount'].mean()
    growth = df['amount'].pct_change().mean() * 100
    
    return {
        "إجمالي المبيعات": total,
        "متوسط اليومي": round(avg, 2),
        "معدل النمو اليومي (%)": round(growth, 2),
        "اتجاه": "إيجابي" if growth > 0 else "سلبي"
    }
