# Generated by Django 3.2.25 on 2024-12-18 17:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_profile_gender'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='Gender',
            new_name='gender',
        ),
    ]
