# Generated by Django 5.1 on 2024-11-03 05:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inquiry', '0004_alter_clientinfo_cli_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='messageinfo',
            name='msg_client',
        ),
        migrations.DeleteModel(
            name='ClientInfo',
        ),
        migrations.DeleteModel(
            name='MessageInfo',
        ),
    ]