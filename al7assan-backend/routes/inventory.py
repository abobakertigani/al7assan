@router.get("/low-stock")
def get_low_stock(company_id: int, db: Session = Depends(get_db)):
    items = db.query(Inventory).filter(Inventory.company_id == company_id).all()
    return {"alerts": get_inventory_analyzer.get_low_stock_alerts(items)}
