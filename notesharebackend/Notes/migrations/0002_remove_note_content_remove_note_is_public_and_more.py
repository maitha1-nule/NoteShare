# Generated by Django 5.0.6 on 2024-06-05 02:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Notes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note',
            name='content',
        ),
        migrations.RemoveField(
            model_name='note',
            name='is_public',
        ),
        migrations.RemoveField(
            model_name='note',
            name='title',
        ),
    ]