# Generated by Django 5.0.6 on 2024-06-09 13:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0003_remove_user_following'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={},
        ),
        migrations.AlterModelTable(
            name='user',
            table='User_user',
        ),
    ]
