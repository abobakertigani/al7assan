# models/__init__.py

# استيراد Base من database (حيث تم تعريفه)
from database import Base

# استيراد النماذج لتكون متاحة عند استيراد models
from .user import User
from .lead import Lead
from .employee import Employee
from .invoice import Invoice

# اختياري: يمكن تجميعها في قائمة
__all__ = ["Base", "User", "Lead", "Employee", "Invoice"]
