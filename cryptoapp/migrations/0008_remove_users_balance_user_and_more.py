# Generated by Django 4.1.3 on 2022-11-14 20:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cryptoapp', '0007_users_balance_user_users_investment_user_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users_balance',
            name='user',
        ),
        migrations.RemoveField(
            model_name='users_investment',
            name='user',
        ),
    ]
