# Generated by Django 3.2.25 on 2024-12-18 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_profile_transaction_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='transaction',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]