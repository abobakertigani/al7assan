# services/customer_classifier.py
def classify_complaint(text: str) -> str:
    text = text.lower()
    if any(word in text for word in ["فاتورة", "دفع", "سعر"]):
        return "finance"
    elif any(word in text for word in ["توصيل", "شحن", "تأخر"]):
        return "logistics"
    elif any(word in text for word in ["جودة", "عطل", "صيانة"]):
        return "technical"
    else:
        return "general"

def generate_auto_reply(category: str) -> str:
    replies = {
        "finance": "شكرًا لتواصلك. نحن نتحقق من مشكلتك المالية وسنتواصل خلال 24 ساعة.",
        "logistics": "نعتذر للتأخير في التوصيل. نعمل على تتبع شحنتك فورًا.",
        "technical": "تم استقبال طلبك الفني. سيراسلوك فريق الدعم قريبًا.",
        "general": "تم استقبال رسالتك. سنرد عليك في أقرب وقت."
    }
    return replies.get(category, "تم استقبال طلبك.")
