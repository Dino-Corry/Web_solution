# Generated by Django 4.1.3 on 2022-11-20 15:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cryptoapp', '0051_alter_request_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users_balanc',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
