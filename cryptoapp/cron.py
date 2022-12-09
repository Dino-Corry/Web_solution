
from django.db import transaction
import requests
from .models import Users_Machine, User, test, Profile, Users_Revenue, Deposit_Request, Users_Balance, Deposit_Records
import logging
logger = logging.getLogger(__name__)

# def create_revenue(request):
#     with transaction.atomic():
#         if Users_Machine.objects.filter(user=request.user).exists():
#             user = request.user
#             x = Users_Machine.objects.get(user=request.user)
#             y = Users_Balance.objects.get(user=request.user)
#             z = Users_Revenue.objects.create(user=user, Name=x.Name, Revenue=x.Profit)
#             revenue = z.Revenue + y.Amount
#             Users_Balance.objects.update(Amount=revenue, user=user)
# receiver(post_save, sender=User)

def test_task(request):
        if Users_Machine.objects.filter(user=request.user).exists():
            test.objects.create(user=request.user, name='Dino')



# def deposit_r(request):
#     if Deposit_Request.objects.filter(user=request.user).exists():
#         deposit = Deposit_Request.objects.get(user=request.user)
#         exiting_balance = Users_Balance.objects.get(user=request.user)
#         if deposit.Approved == True():
#             user = request.user
#             balance = float(deposit.Deposit_Amount) + exiting_balance.Amount
#             Users_Balance.objects.update(Amount=balance, user=user)
#             Deposit_Request.objects.filter(user).delete()
            

