# Generated by Django 4.1.3 on 2022-11-19 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cryptoapp', '0037_request_date_alter_request_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Withdrawal_password',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]