from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('buy_machines', views.buy_machines, name='buy_machines'),
    path('withdrawals', views.withdrawals, name='withdrawals'),
    path('withdrawal_password', views.withdrawal_password, name='withdrawal_password'),
    path('deposit', views.Deposits, name='deposit'),
    path('history', views.history, name='history'),
    path('my-machines', views.my_machines, name='my-machines'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)