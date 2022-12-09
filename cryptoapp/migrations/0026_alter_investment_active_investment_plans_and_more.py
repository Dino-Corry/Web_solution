# Generated by Django 4.1.3 on 2022-11-16 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cryptoapp', '0025_alter_balance_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='investment',
            name='Active_Investment_Plans',
            field=models.CharField(default='0', max_length=30),
        ),
        migrations.AlterField(
            model_name='investment',
            name='Total_Plans',
            field=models.CharField(default='0', max_length=30),
        ),
        migrations.AlterField(
            model_name='users_balanc',
            name='Amount',
            field=models.FloatField(default=0.0, max_length=4),
        ),
        migrations.AlterField(
            model_name='users_balanc',
            name='Bonus',
            field=models.FloatField(default=10.0, max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='users_balanc',
            name='Deposit',
            field=models.FloatField(default=0.0, max_length=30),
        ),
        migrations.AlterField(
            model_name='users_balanc',
            name='Profit',
            field=models.FloatField(default=0.0, max_length=30),
        ),
        migrations.AlterField(
            model_name='users_balanc',
            name='Referral_Bonus',
            field=models.FloatField(default=0.0, max_length=30),
        ),
        migrations.AlterField(
            model_name='users_balanc',
            name='Withdrawals',
            field=models.FloatField(default=0.0, max_length=30),
        ),
        migrations.DeleteModel(
            name='Balance',
        ),
    ]
