# Generated by Django 4.1.3 on 2022-11-20 20:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cryptoapp', '0056_alter_withdrawal_request_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='withdrawal_request',
            old_name='Apprroved',
            new_name='Approved',
        ),
    ]
