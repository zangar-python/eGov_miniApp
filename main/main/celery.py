from celery.schedules import crontab
import celery
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE","main.settings")

app = celery.Celery(
    "main",
    backend="redis://localhost:6379/0",
    broker="redis://localhost:6379/0"
)

app.autodiscover_tasks()