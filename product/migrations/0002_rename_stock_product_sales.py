# Generated by Django 3.2.25 on 2024-12-19 06:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='stock',
            new_name='sales',
        ),
    ]
