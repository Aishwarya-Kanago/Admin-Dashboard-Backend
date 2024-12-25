# Generated by Django 3.2.25 on 2024-12-25 16:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.CharField(blank=True, max_length=500, null=True)),
                ('bio', models.TextField(blank=True, null=True)),
                ('designation', models.CharField(blank=True, max_length=250, null=True)),
                ('status', models.CharField(blank=True, max_length=250, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True)),
                ('account_name', models.CharField(blank=True, max_length=250, null=True)),
                ('account_open_date', models.CharField(blank=True, max_length=15, null=True)),
                ('location', models.CharField(blank=True, max_length=250, null=True)),
                ('transaction', models.IntegerField(blank=True, default=0, null=True)),
                ('transaction_status', models.CharField(blank=True, max_length=15, null=True)),
                ('gender', models.CharField(blank=True, max_length=15, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
