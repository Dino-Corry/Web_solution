# Generated by Django 4.1.3 on 2022-11-14 20:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cryptoapp', '0010_alter_users_balance_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users_balance',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
