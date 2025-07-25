# services/ai_agent.py
def parse_command(command: str, user_role: str):
    command = command.strip().lower()
    
    if "تقرير" in command and "مبيعات" in command:
        return {"action": "generate_report", "report": "sales", "target": "manager"}
    elif "أمر شراء" in command or "اشترِ" in command:
        return {"action": "create_purchase_order", "items": extract_items(command)}
    elif "عدد" in command and "موظفين" in command:
        return {"action": "query", "data": "new_employees_count"}
    else:
        return {"action": "unknown", "suggestions": ["أرسل تقرير المبيعات", "أنشئ أمر شراء", "كم عدد الفواتير غير المسددة؟"]}

def extract_items(text):
    # بسيط جدًا — يمكن تحسينه لاحقًا
    words = text.split()
    return [word for word in words if len(word) > 3 and word not in ["أمر", "شراء", "اشترِ"]]
