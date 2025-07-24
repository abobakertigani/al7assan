# routes/auth.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import Annotated
from database import get_db
from models.user import User
from schemas.auth import LoginSchema
from utils.security import verify_password

router = APIRouter()

@router.post("/login")
def login(data: LoginSchema, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == data.email).first()
    if not user or not verify_password(data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="بريد إلكتروني أو كلمة مرور خاطئة"
        )
    return {"message": "تم تسجيل الدخول بنجاح", "user_id": user.id, "role": user.role}
