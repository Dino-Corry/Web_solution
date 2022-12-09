from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

# setting the Django settings module.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cryptosite.settings')
app = Celery('cryptosite')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.update(timezone= 'Africa/Lagos')
app.autodiscover_tasks()
app.conf.beat_schedule = {
    'update_all_api':{
        'task':'cryptoapp.tasks.test_task',
        'schedule': crontab(minute=1, hour=0)
    }
}


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
