# schemas/auth.py
from pydantic import BaseModel
from typing import Optional

# للدخول
class LoginSchema(BaseModel):
    email: str
    password: str

# للتسجيل
class SignupSchema(BaseModel):
    name: str
    email: str
    password: str
    company_name: str
    company_email: Optional[str] = None
    company_phone: Optional[str] = None
    company_address: Optional[str] = None
