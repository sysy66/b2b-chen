# Generated by Django 5.1 on 2024-10-31 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_alter_category_desc_alter_item_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
    ]