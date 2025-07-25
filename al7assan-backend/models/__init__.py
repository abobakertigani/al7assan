# models/__init__.py
from database import Base

from .user import User
from .lead import Lead
from .employee import Employee
from .invoice import Invoice
from .company import Company  # ✅ أضف هذا السطر

__all__ = [
    "Base",
    "User",
    "Lead",
    "Employee",
    "Invoice",
    "Company"
]
