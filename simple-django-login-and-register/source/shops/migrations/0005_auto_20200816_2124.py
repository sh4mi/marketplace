# Generated by Django 2.2.13 on 2020-08-16 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0004_product_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(default='', unique=True),
        ),
    ]
