from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from django.db import transaction
from datetime import datetime
#from .tasks import test_task

# Create your models here.
    

class Users_Balance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Amount = models.FloatField(max_length=4, default=0.0)
    Profit = models.FloatField(max_length=30, default=0.0)
    Bonus = models.FloatField(max_length=30, default=10.0)
    Referral_Bonus = models.FloatField(max_length=30, default=0.00)
    Deposit = models.FloatField(max_length=30, default=0.00)
    Withdrawals = models.FloatField(max_length=30, default=0.00)
    date = models.DateTimeField(default=datetime.now, blank=True)
    
    def __str__(self):
        return self.user.username
    
    
class test(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    
    # def test_ob(self):
    #     test_task.delay()
    
class Investment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Total_Plans = models.CharField(max_length=30, default='0')
    Active_Investment_Plans = models.CharField(max_length=30, default='0')
    
    def __str__(self):
        return f'{self.user.username} Investment'
    

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    
    def __str__(self):
        return f'{self.user.username} Profile'

class Basic_Machines(models.Model):
    Image = models.ImageField(default='default_miner.png', upload_to='profile_pics')
    Name = models.CharField(max_length=20)
    Price = models.FloatField(max_length=10)
    Profit = models.CharField(max_length=40)
    
    def __str__(self):
        return self.Name
    

class Deluxe_Machines(models.Model):
    Image = models.ImageField(default='default_miner.png', upload_to='profile_pics')
    Name = models.CharField(max_length=20)
    Price = models.FloatField(max_length=10)
    Profit = models.CharField(max_length=40)
    
    def __str__(self):
        return self.Name    
    

class Exclusive_Machines(models.Model):
    Image = models.ImageField(default='default_miner.png', upload_to='profile_pics')
    Name = models.CharField(max_length=20)
    Price = models.FloatField(max_length=10)
    Profit = models.CharField(max_length=40)
    
    def __str__(self):
        return self.Name
    
    
class Deposit_Records(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Deposit_Amount = models.FloatField(max_length=30)
    Approved = models.BooleanField(default=False)
    Date = models.DateTimeField(default=datetime.now, blank=True)
    
    def __str__(self):
        return f'{self.user} Deposit_Records'
        
    
class Deposit_Request(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Deposit_Amount = models.FloatField(max_length=30)
    Approved = models.BooleanField(default=False)
    Date = models.DateTimeField(default=datetime.now, blank=True)

                    
    def __str__(self):
        return f'{self.user} Deposit'
    
    


class Withdrawal_Request(models.Model):
    date = models.DateTimeField(default=datetime.now, blank=True)
    Request_Amount = models.FloatField(max_length=30)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Wallet_Address = models.CharField(max_length=100)
    Charges = models.FloatField(max_length=200)
    Fund_Sent= models.BooleanField(default=False)
    Return_Amount = models.FloatField(max_length=20)
    
    
    def __str__(self):
        return f'{self.user} Withdrawal_Request'
    
class Withdrawal_password(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    password3 = models.CharField(max_length=100)
    Wallet_Address = models.CharField(max_length=100)
    
    def __str__(self):
        return f'{self.user} Password'
    
    
class Users_Machine(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Name = models.CharField(max_length=20)
    Price = models.FloatField(max_length=100)
    Profit = models.FloatField(max_length=100)
    Revenue = models.FloatField(max_length=20)
    date = models.DateTimeField(default=datetime.now, blank=True)
    
    def __str__(self):
        return f'{self.user} Machine'
    
class Users_Revenue(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Name = models.CharField(max_length=20)
    Revenue = models.FloatField(max_length=20)
    date = models.DateTimeField(default=datetime.now, blank=True)
    
    def __str__(self):
        return f'{self.user} Revenue'
    

    
    