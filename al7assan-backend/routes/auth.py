# routes/auth.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from jose import jwt, JWTError
from datetime import datetime, timedelta
from typing import Optional
import database
from models import User, Company
from schemas.auth import LoginSchema, SignupSchema
from utils.security import verify_password, hash_password

router = APIRouter(prefix="/auth", tags=["Authentication"])

# إعدادات JWT
SECRET_KEY = "your-super-secret-key-change-in-production"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=15))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

@router.post("/login")
def login(form: LoginSchema, db: Session = Depends(database.get_db)):
    user = db.query(User).filter(User.email == form.email).first()
    if not user or not verify_password(form.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="بريد إلكتروني أو كلمة مرور غير صحيحة",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token = create_access_token(
        data={
            "sub": user.email,
            "user_id": user.id,
            "company_id": user.company_id,
            "role": user.role
        }
    )
    
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "user": {
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "role": user.role,
            "company_id": user.company_id
        }
    }

@router.post("/signup")
def signup(data: SignupSchema, db: Session = Depends(database.get_db)):
    # تحقق من وجود الشركة
    company = db.query(Company).filter(Company.name == data.company_name).first()
    if not company:
        company = Company(
            name=data.company_name,
            email=data.company_email,
            phone=data.company_phone,
            address=data.company_address
        )
        db.add(company)
        db.commit()
        db.refresh(company)

    # تحقق من وجود المستخدم
    existing = db.query(User).filter(User.email == data.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="البريد الإلكتروني مسجل مسبقًا")

    hashed = hash_password(data.password)

    new_user = User(
        name=data.name,
        email=data.email,
        hashed_password=hashed,
        role="owner",
        company_id=company.id
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    # إنشاء توكن تلقائيًا
    access_token = create_access_token(data={"sub": new_user.email, "user_id": new_user.id, "company_id": new_user.company_id})

    return {
        "access_token": access_token,
        "token_type": "bearer",
        "user": {
            "id": new_user.id,
            "name": new_user.name,
            "email": new_user.email,
            "role": new_user.role,
            "company_id": new_user.company_id
        }
    }
