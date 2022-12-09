# Generated by Django 4.1.3 on 2022-11-20 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cryptoapp', '0058_users_balance_delete_users_balanc'),
    ]

    operations = [
        migrations.RenameField(
            model_name='withdrawal_request',
            old_name='Charge',
            new_name='Charges',
        ),
        migrations.RenameField(
            model_name='withdrawal_request',
            old_name='Amount',
            new_name='Request_Amount',
        ),
        migrations.AddField(
            model_name='withdrawal_request',
            name='Return_Amount',
            field=models.FloatField(default=0, max_length=200),
            preserve_default=False,
        ),
    ]
