
from django.contrib.auth.models import User
from .models import Users_Machine, test
#from celery import shared_task
from celery import shared_task


@shared_task(bind=True)
def test_task():
    #if Users_Machine.objects.filter().exists():
    test.objects.create(name='Dinoo', user='u.user')