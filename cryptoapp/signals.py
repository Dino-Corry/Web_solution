from django.db.models.signals import post_save, pre_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile, Users_Balance, Investment
from django.conf import settings
from django.db import transaction
from datetime import datetime

from .models import Users_Machine, Users_Revenue, Deposit_Request, Users_Balance, Deposit_Records



@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    instance.profile.save()
    
@receiver(post_save, sender=User)
def create_users_balance(sender, instance, created, **kwargs):
    if created:
        Users_Balance.objects.create(user=instance)

@receiver(post_save, sender=User)
def create_investment(sender, instance, created, **kwargs):
    if created:
        Investment.objects.create(user=instance)
        
# @receiver(post_save, sender=User)
# def deposit(*args, instance, **kwargs):
#     if Deposit_Request.objects.exists():
#         deposit = Deposit_Request.objects.last()
#         with transaction.atomic():
#             if deposit.Approved == True:
#                 exiting_balance = Users_Balance.objects.get()
#                 balance = deposit.Deposit_Amount + exiting_balance.Amount
#                 Users_Balance.objects.update(Amount=balance, user=instance)
#                 Deposit_Request.objects.last().delete()
