# Generated by Django 5.1 on 2024-10-31 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inquiry', '0002_remove_clientinfo_is_active'),
    ]

    operations = [
        migrations.RenameField(
            model_name='messageinfo',
            old_name='updated_at',
            new_name='dealt_at',
        ),
        migrations.AddField(
            model_name='messageinfo',
            name='is_deal',
            field=models.BooleanField(default=False),
        ),
    ]
