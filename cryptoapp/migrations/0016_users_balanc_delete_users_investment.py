# Generated by Django 4.1.3 on 2022-11-14 21:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cryptoapp', '0015_rename_users_balance_balance'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users_Balanc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Amount', models.FloatField(default=0, max_length=4)),
                ('Profit', models.FloatField(default=0, max_length=30)),
                ('Bonus', models.FloatField(default=0, max_length=30)),
                ('Referral_Bonus', models.FloatField(default=0, max_length=30)),
                ('Deposit', models.FloatField(default=0, max_length=30)),
                ('Withdrawals', models.FloatField(default=0, max_length=30)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Users_Investment',
        ),
    ]