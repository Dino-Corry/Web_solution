# Generated by Django 4.1.3 on 2022-12-04 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cryptoapp', '0080_rename_deposit_deposit_request_users_revenue_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='deposit_records',
            name='Approved',
            field=models.BooleanField(default=False),
        ),
    ]
