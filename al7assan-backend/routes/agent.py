# routes/agent.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import database
from services.ai_agent import parse_command

router = APIRouter(prefix="/agent", tags=["AI Agent"])

@router.post("/command")
def execute_command(
    text: str,
    user_role: str = "user",
    company_id: int = None,
    db: Session = Depends(database.get_db)
):
    """
    إرسال أمر للمساعد الرقمي (مثال: "أنشئ أمر شراء"، "أرسل تقرير")
    """
    result = parse_command(text, user_role)
    
    # هنا يمكن ربط النتيجة بتنفيذ فعلي (في إصدار لاحق)
    # مثلاً: إذا كان action = "create_purchase_order"، نُنشئ أمر شراء تلقائيًا
    
    return {
        "command": text,
        "interpreted": result,
        "status": "تم التحليل - التنفيذ قادم في الإصدار التالي"
    }

@router.get("/capabilities")
def get_capabilities():
    """
    عرض الأوامر التي يفهمها المساعد
    """
    return {
        "understands": [
            "أرسل تقرير المبيعات",
            "أنشئ أمر شراء لـ [المنتج]",
            "كم عدد الموظفين الجدد؟",
            "ما الفواتير غير المسددة؟",
            "هل هناك تنبيهات المخزون؟"
        ],
        "future": ["التحكم الصوتي", "الإشعارات التلقائية", "التواصل مع الفرق"]
    }
