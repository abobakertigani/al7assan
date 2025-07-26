# services/it_monitor.py
import psutil
import datetime

def get_system_health():
    return {
        "cpu_usage": psutil.cpu_percent(),
        "memory_usage": psutil.virtual_memory().percent,
        "disk_usage": psutil.disk_usage('/').percent,
        "status": "تحذير" if psutil.cpu_percent() > 80 else "مستقر",
        "last_check": datetime.datetime.now().isoformat()
    }
