import os
from celery import Celery
from celery.schedules import crontab

# Указываем Django настройки
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

app = Celery("reservationtable")

# Загружаем конфигурацию из Django settings
app.config_from_object("django.conf:settings", namespace="CELERY")

# Автоматическое обнаружение задач во всех приложениях Django
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f"Request: {self.request!r}")


# Настройки периодических задач
app.conf.beat_schedule = {
    "send_booking_reminders_daily": {
        "task": "reservations.tasks.send_booking_reminders",
        "schedule": crontab(hour=9, minute=0),  # Запуск каждый день в 9 утра
    },
}
