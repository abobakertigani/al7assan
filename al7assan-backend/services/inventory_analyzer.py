# services/inventory_analyzer.py
def get_low_stock_alerts(inventory_items):
    alerts = []
    for item in inventory_items:
        if item.current_stock <= item.min_stock:
            alerts.append({
                "product": item.product_name,
                "current": item.current_stock,
                "min": item.min_stock,
                "supplier": item.supplier,
                "suggest_order": item.min_stock * 2 - item.current_stock
            })
    return alerts
