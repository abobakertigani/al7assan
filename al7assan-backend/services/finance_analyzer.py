# services/finance_analyzer.py
import pandas as pd
from sklearn.linear_model import LinearRegression
from datetime import datetime, timedelta
import numpy as np

def predict_cash_flow(invoices_data, days_ahead=30):
    """
    invoices_data: قائمة من الشكل:
    [
      {"date": "2025-04-01", "amount": 5000, "status": "paid"},
      ...
    ]
    """
    if not invoices_data:
        return {"error": "لا توجد بيانات كافية"}

    # تحويل إلى DataFrame
    df = pd.DataFrame(invoices_data)
    df['date'] = pd.to_datetime(df['date'])
    df = df[df['status'] == 'paid']  # نستخدم فقط الفواتير المدفوعة
    df = df.sort_values('date')

    if len(df) < 2:
        return {"error": "يحتاج النظام إلى فاتورتين على الأقل"}

    # تحويل التاريخ إلى رقم (أيام من أول تاريخ)
    df['day'] = (df['date'] - df['date'].min()).dt.days
    X = df['day'].values.reshape(-1, 1)
    y = df['amount'].values

    # تدريب النموذج
    model = LinearRegression()
    model.fit(X, y)

    # التنبؤ للأيام القادمة
    last_day = X[-1][0]
    future_days = np.array([[last_day + i] for i in range(1, days_ahead + 1)])
    predictions = model.predict(future_days)

    total_predicted = round(predictions.sum(), 2)

    return {
        "predicted_cash_in_next_30_days": total_predicted,
        "daily_average": round(predictions.mean(), 2),
        "trend": "صاعد" if model.coef_[0] > 0 else "هابط",
        "slope": round(model.coef_[0], 2)
    }
