# Generated by Django 5.0.6 on 2024-06-01 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='lat_login',
        ),
        migrations.AlterField(
            model_name='account',
            name='last_login',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
