# Generated by Django 3.2.25 on 2024-12-19 06:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_rename_stock_product_sales'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='sales',
            new_name='stock',
        ),
    ]
