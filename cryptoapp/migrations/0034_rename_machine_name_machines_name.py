# Generated by Django 4.1.3 on 2022-11-17 00:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cryptoapp', '0033_alter_machines_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='machines',
            old_name='Machine_Name',
            new_name='Name',
        ),
    ]
