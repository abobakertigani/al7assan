# models/__init__.py
from database import Base

from .user import User
from .company import Company
from .employee import Employee
from .invoice import Invoice
from .lead import Lead
from .inventory import Inventory
from .support_ticket import SupportTicket
from .production_record import ProductionRecord
from .sale import Sale
from .quality_check import QualityCheck

__all__ = [
    "Base",
    "User",
    "Company",
    "Employee",
    "Invoice",
    "Lead",
    "Inventory",
    "SupportTicket",
    "ProductionRecord",
    "Sale",
    "QualityCheck"
]
