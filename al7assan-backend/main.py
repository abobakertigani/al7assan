# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import auth, hr, finance  # سننشئها لاحقًا
from routes import inventory, support, production, agent
from database import engine
from models import Base
from modules.aquaculture.routes import router as aquaculture_router

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

app.include_router(auth.router, prefix="/api")
app.include_router(hr.router, prefix="/api")
app.include_router(finance.router, prefix="/api")
app.include_router(leads.router, prefix="/api")
app.include_router(inventory.router, prefix="/api")
app.include_router(support.router, prefix="/api")
app.include_router(production.router, prefix="/api")
app.include_router(agent.router, prefix="/api") 
app.include_router(aquaculture_router, prefix="/api")

def root():
    return {"message": "مرحبًا بكم في نظام الإحسان - Backend يعمل!"}
