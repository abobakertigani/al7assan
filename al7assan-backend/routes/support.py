@router.post("/ticket")
def create_ticket(text: str, customer_name: str, db: Session = Depends(get_db)):
    category = customer_classifier.classify_complaint(text)
    reply = customer_classifier.generate_auto_reply(category)

    # يمكن حفظ التذكرة في قاعدة البيانات
    return {
        "status": "تم الإنشاء",
        "category": category,
        "auto_reply": reply
    }
