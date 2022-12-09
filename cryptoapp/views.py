
from django.shortcuts import render, redirect
from .models import Investment, Withdrawal_password, Deposit_Records, Deposit_Request, Users_Machine, Withdrawal_Request, Users_Balance, Basic_Machines, Deluxe_Machines, Exclusive_Machines
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import transaction
# Create your views here.

@login_required(login_url='/login')
def buy_machines(request):
    if request.method == 'POST':
        user = request.user
        machine_name = request.POST['machine_name']
        machine_price = request.POST['price']
        machine_profit = request.POST['profit']
        user_balance = Users_Balance.objects.get(user=request.user)
        with transaction.atomic():
            if float(machine_price) < user_balance.Amount:
                after_invest = user_balance.Amount - float(machine_price)
                Users_Balance.objects.update(Amount=after_invest, user=user)
                messages.success(request, 'Request sucessful')
                Users_Machine.objects.create(Profit=machine_profit, Price=machine_price, Name=machine_name, user=user, Revenue=0)
                return redirect('buy_machines')
            else:
                messages.warning(request, 'Insufficient fund')
                return redirect('buy_machines')
    else:
        machine1 = Basic_Machines.objects.all()
        machine2 = Deluxe_Machines.objects.all()
        return render(request, 'buy_machines.html', {'machine1': machine1, 'machine2': machine2})


    
@login_required(login_url='/login')
def Deposits(request):
    if request.method == 'POST':
        D_Amount = request.POST['Input_Amount']
        user = request.user
        Deposit_R = Deposit_Request.objects.create(Deposit_Amount=D_Amount, user=user)
        Deposit_R.save()
        Deposit_C = Deposit_Records.objects.create(Deposit_Amount=D_Amount, user=user)
        Deposit_C.save()
        messages.warning(request, 'Request sent. Wait for comfirmation')
        return redirect('deposit')
        
    else:
        return render(request, 'deposit.html')

       
@login_required(login_url='/login')
def withdrawals(request, *args, **kwargs):
    if request.method == 'POST':
        Input_Amount = request.POST['Input_Amount']
        user = request.user
        input_password = request.POST['password']
        total = Users_Balance.objects.get(user=request.user)
        
        if Withdrawal_password.objects.filter(user=request.user).exists():
            password = Withdrawal_password.objects.get(user=request.user)
            if password.password3 == input_password:
                if int(Input_Amount) > 99:
                    if (total.Amount >= float(Input_Amount)):
                        charges = float(30) * float(Input_Amount) / float(100)
                        returns = float(Input_Amount) - charges
                        New_Request = Withdrawal_Request.objects.create(user=user, Wallet_Address=password.Wallet_Address, Request_Amount=Input_Amount, Return_Amount=returns, Charges=charges)
                        New_Request.save
                        calculations = total.Amount - float(Input_Amount)
                        total_withdraw = total.Withdrawals + float(Input_Amount)
                        Users_Balance.objects.update(Amount=calculations, Withdrawals=total_withdraw, user=user)
                        
                        messages.success(request, 'Request sent successful')
                        return redirect('withdrawals')
                    else:
                        messages.warning(request, 'Insufficient funds')
                        return redirect('withdrawals')
                else:
                        messages.warning(request, 'Sorry, your withdrawal is below 100TRX')
                        return redirect('withdrawals')
            else:
                messages.warning(request, 'Sorry, your withdrawal password is not correct')
                return redirect('withdrawals')
        else:
            messages.warning(request, 'Sorry, you haven\'t create a withdrawal password yet.')
            return redirect('withdrawals')
    else:
        balance = Users_Balance.objects.filter(user=request.user)
        return render(request, 'withdrawals.html', {'balance': balance})

@login_required(login_url='/login')
def withdrawal_password(request):
    if request.method == 'POST':
        password3 = request.POST['password3']
        password4 = request.POST['password4']
        user = request.user
        Wallet_Address = request.POST['address']
        
        if password3 == password4:
            if Withdrawal_password.objects.filter(user=request.user).exists():
                messages.warning(request, 'Sorry you\'ve already created withdrawal password')
                return redirect('withdrawal_password')
            else:
                password3 = Withdrawal_password.objects.create(Wallet_Address=Wallet_Address, password3=password3, user=user)
                password3.save()
                messages.success(request, 'Successful')
                return redirect('withdrawal_password')
        else:
            messages.warning(request, 'Sorry, password doesn\'t match')
            return redirect('withdrawal_password')
    else:
        return render(request, 'withdrawal_password.html')


# @login_required(login_url='/login')
# def deposit(request):
#     total = Users_Balance.objects.filter(user=request.user)
#     return render(request, 'deposit.html', {'total': total})


def register(request):
    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']
        
        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Sorry, email is already in used')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Sorry, username is already in used')
                return redirect('register')
            else:
                user = User.objects.create_user(email=email, username=username, password=password)
                user.save()
                messages.success(request, 'Registration successful, please login')
                return redirect('login')
        else:
            messages.info(request, 'Sorry, password doesn\'t match')
            return redirect('register')
        
    else:
        return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            return redirect('dashboard')
        else:
            messages.info(request, 'Sorry, invalid credentials. \nPlease chech your details.')
            return redirect('login')
            
    return render(request, 'login.html')

@login_required(login_url='/login')
def dashboard(request):
    total = Users_Balance.objects.filter(user=request.user)
    invest = Investment.objects.filter(user=request.user)
    return render(request, 'dashboard.html', {'total': total, 'invest': invest})

@login_required(login_url='/login')
def history(request):
    record = Withdrawal_Request.objects.filter(user=request.user)
    total = Users_Balance.objects.filter(user=request.user)
    deposit = Deposit_Records.objects.filter(user=request.user)
    return render(request, 'history.html', {'record': record, 'total': total, 'deposits': deposit,})

def logout(request):
    auth.logout(request)
    return redirect('/')

@login_required(login_url='/login')
def my_machines(request):
    machine1 = Basic_Machines.objects.all()
    machine2 = Deluxe_Machines.objects.all()
    return render(request, 'my-machines.html', {'machine1': machine1, 'machine2': machine2})