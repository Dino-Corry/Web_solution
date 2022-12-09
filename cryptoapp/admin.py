from django.contrib import admin
from django.contrib.auth.models import User
from .models import Withdrawal_password, Users_Machine, Deposit_Request, Users_Balance
from .models import Profile, Investment, Basic_Machines, Deluxe_Machines, Exclusive_Machines 
from .models import Withdrawal_Request, test, Users_Revenue, Deposit_Records

# Register your models here.
admin.site.register(Profile),
admin.site.register(Investment),
admin.site.register(Deluxe_Machines),
admin.site.register(Exclusive_Machines),
admin.site.register(Withdrawal_password),
admin.site.register(test),


@admin.register(Withdrawal_Request)
class Withdrawal_Request(admin.ModelAdmin):
    list_display = ('user', 'Return_Amount', 'Charges', 'Wallet_Address', 'Fund_Sent')

@admin.register(Users_Balance)
class Users_Balance(admin.ModelAdmin):
    list_display = ('user', 'Amount', 'Withdrawals', 'Bonus', 'Deposit')
    
@admin.register(Deposit_Request)
class Deposit_Request(admin.ModelAdmin):
    list_display = ('user', 'Deposit_Amount', 'Approved', 'Date')
    ordering = ('-Date',)
    search_fields = ('user__username', 'Deposit_Amount',)
    
@admin.register(Users_Machine)
class Users_Machine(admin.ModelAdmin):
    list_display = ('user', 'Name', 'Price')
    
@admin.register(Users_Revenue)
class Users_Revenue(admin.ModelAdmin):
    list_display = ('user', 'Name', 'Revenue')

@admin.register(Deposit_Records)
class Deposit_Records(admin.ModelAdmin):
    list_display = ('user', 'Deposit_Amount', 'Approved', 'Date')
    ordering = ('-Date',)
    search_fields = ('user__username', 'Deposit_Amount',)