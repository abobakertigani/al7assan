from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.auth import LoginSchema
from models.user import User
from utils.security import hash_password
from database import get_db

router = APIRouter()

@router.post("/signup")
def signup(
    name: str,
    email: str,
    password: str,
    company_name: str,
    db: Session = Depends(get_db)
):
    # تحقق من عدم وجود مستخدم بنفس البريد
    existing = db.query(User).filter(User.email == email).first()
    if existing:
        raise HTTPException(status_code=400, detail="البريد الإلكتروني مسجل مسبقًا")

    hashed = hash_password(password)

    new_user = User(
        name=name,
        email=email,
        hashed_password=hashed,
        role="owner"
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"message": "تم التسجيل بنجاح", "user_id": new_user.id}
