# Generated by Django 4.1.3 on 2022-12-04 00:49

import datetime
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cryptoapp', '0079_users_machine_date'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Deposit',
            new_name='Deposit_Request',
        ),
        migrations.AddField(
            model_name='users_revenue',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
