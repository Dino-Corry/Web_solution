# Generated by Django 4.1.3 on 2022-11-19 13:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cryptoapp', '0039_rename_password_withdrawal_password_password3'),
    ]

    operations = [
        migrations.RenameField(
            model_name='withdrawal_password',
            old_name='password3',
            new_name='username',
        ),
        migrations.RemoveField(
            model_name='withdrawal_password',
            name='user',
        ),
    ]
