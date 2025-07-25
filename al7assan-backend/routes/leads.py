# routes/leads.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import database
import models

router = APIRouter()

# إنشاء الجدول إذا لم يكن موجودًا
models.Base.metadata.create_all(bind=database.engine)

@router.post("/leads")
async def capture_lead(
    lead_dict,
    db: Session = Depends(database.get_db)
):
    try:
        # إنشاء كائن جديد
        new_lead = models.Lead(
            name=lead_data['name'],
            email=lead_data['email'],
            phone=lead_data['phone'],
            field=lead_data['field'],
            package=lead_data['package'],
            message=lead_data['message'],
            timestamp=lead_data['timestamp']
        )
        db.add(new_lead)
        db.commit()
        db.refresh(new_lead)
        return {"status": "success", "message": "تم حفظ الطلب", "id": new_lead.id}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"خطأ داخلي: {str(e)}")
