# Generated by Django 5.1 on 2024-10-31 04:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inquiry', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clientinfo',
            name='is_active',
        ),
    ]
