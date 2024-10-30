# Generated by Django 5.1 on 2024-10-29 04:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('name',), 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='item',
            options={'ordering': ('name',)},
        ),
        migrations.RemoveField(
            model_name='category',
            name='identifier',
        ),
        migrations.RemoveField(
            model_name='item',
            name='identifier',
        ),
        migrations.AddField(
            model_name='item',
            name='colour',
            field=models.CharField(choices=[('General', 'General'), ('10mm', '10mm'), ('20mm', '20mm'), ('30mm', '30mm')], default='General', max_length=50),
        ),
        migrations.AddField(
            model_name='item',
            name='size',
            field=models.CharField(choices=[('General', 'General'), ('10mm', '10mm'), ('20mm', '20mm'), ('30mm', '30mm')], default='General', max_length=50),
        ),
        migrations.AddField(
            model_name='item',
            name='thickness',
            field=models.CharField(choices=[('General', 'General'), ('10mm', '10mm'), ('20mm', '20mm'), ('30mm', '30mm')], default='General', max_length=50),
        ),
        migrations.AlterField(
            model_name='category',
            name='desc',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='products.category'),
        ),
        migrations.AlterField(
            model_name='item',
            name='desc',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='img',
            field=models.ImageField(default='images/products/default.jpg', upload_to='images/products/'),
        ),
    ]