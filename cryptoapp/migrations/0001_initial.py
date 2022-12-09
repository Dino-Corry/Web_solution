# Generated by Django 4.1.3 on 2022-11-10 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Amount', models.FloatField(max_length=4)),
                ('Profit', models.FloatField(max_length=4)),
                ('Bonus', models.FloatField(max_length=4)),
                ('Referral_Bonus', models.FloatField(max_length=4)),
                ('Deposit', models.FloatField(max_length=4)),
                ('Withdrawals', models.FloatField(max_length=4)),
            ],
        ),
    ]
