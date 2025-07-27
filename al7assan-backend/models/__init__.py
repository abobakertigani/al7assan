# models/__init__.py

from database import Base

# استيراد النماذج
from .user import User
from .lead import Lead
from .employee import Employee
from .invoice import Invoice
from .company import Company
from .inventory import Inventory           # ✅ أضف هذا السطر
from .support_ticket import SupportTicket  # ✅ إذا أنشأتها
from .production_record import ProductionRecord  # ✅ إذا أنشأتها
from .quality_check import QualityCheck    # ✅ إذا أنشأتها
from .sale import Sale                     # ✅ إذا أنشأتها

# جعلها متاحة عند الاستيراد
__all__ = [
    "Base",
    "User",
    "Lead",
    "Employee",
    "Invoice",
    "Company",
    "Inventory",           # ✅ أضفها هنا
    "SupportTicket",
    "ProductionRecord",
    "QualityCheck",
    "Sale"
]
