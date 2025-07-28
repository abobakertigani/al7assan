# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import auth, hr, finance  # سننشئها لاحقًا
from routes import inventory, support, production, agent
from database import engine
from models import Base
# استيراد وحدات الأقسام المخصصة
from modules.aquaculture.routes import router as aquaculture_router
from modules.manufacturing.routes import router as manufacturing_router
from modules.solar.routes import router as solar_router
from modules.construction.routes import router as construction_router
from modules.education.routes import router as education_router
from modules.hse.routes import router as hse_router
from modules.logistics.routes import router as logistics_router
from modules.hospitality.routes import router as hospitality_router
from modules.security.routes import router as security_router
from modules.trading.routes import router as trading_router
# إنشاء جميع الجداول
Base.metadata.create_all(bind=engine)

app = FastAPI(title="نظام الإحسان - Backend", version="1.0")

# تفعيل CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # غيرها لاحقًا إلى نطاق موقعك
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ربط المسارات
from routes import leads  

# ربط الـ Routers
app.include_router(auth.router, prefix="/api")
app.include_router(hr.router, prefix="/api")
app.include_router(finance.router, prefix="/api")
app.include_router(leads.router, prefix="/api")
app.include_router(inventory.router, prefix="/api")
app.include_router(support.router, prefix="/api")
app.include_router(production.router, prefix="/api")
app.include_router(agent.router, prefix="/api") 

# الأقسام المخصصة
app.include_router(aquaculture_router, prefix="/api")
app.include_router(manufacturing_router, prefix="/api")
app.include_router(solar_router, prefix="/api")
app.include_router(construction_router, prefix="/api")
app.include_router(education_router, prefix="/api")
app.include_router(hse_router, prefix="/api")
app.include_router(logistics_router, prefix="/api")
app.include_router(hospitality_router, prefix="/api")
app.include_router(security_router, prefix="/api")
app.include_router(trading_router, prefix="/api") 

def root():
    return {"message": "مرحبًا بكم في نظام الإحسان - Backend يعمل!"}
