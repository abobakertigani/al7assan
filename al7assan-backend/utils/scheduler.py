# utils/scheduler.py
import schedule
import time
from threading import Thread

def send_daily_report():
    print("جاري إرسال تقرير يومي للإدارة...")

# جدولة المهمة
schedule.every().day.at("08:00").do(send_daily_report)

def run_scheduler():
    while True:
        schedule.run_pending()
        time.sleep(60)

# شغّل المجدول في خيط منفصل
thread = Thread(target=run_scheduler)
thread.start()
