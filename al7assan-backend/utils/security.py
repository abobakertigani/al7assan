# utils/security.py
from passlib.context import CryptContext

# نُهيئ أداة تشفير كلمات المرور
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    """
    تشفير كلمة المرور
    """
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    التحقق من أن كلمة المرور المدخلة تطابق المُشفرة
    """
    return pwd_context.verify(plain_password, hashed_password)
