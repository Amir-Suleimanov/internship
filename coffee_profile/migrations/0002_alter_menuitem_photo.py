# Generated by Django 4.2 on 2024-04-22 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coffee_profile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='static/menu_items/', verbose_name='Фото'),
        ),
    ]
