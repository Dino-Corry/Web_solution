# Generated by Django 3.2.16 on 2022-12-07 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cryptoapp', '0088_alter_test_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='user',
            field=models.CharField(max_length=100),
        ),
    ]
