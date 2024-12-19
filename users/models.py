from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_pic = models.CharField(max_length=500,blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    designation = models.CharField(max_length=250, blank=True, null=True)
    status = models.CharField(max_length=250, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    account_name = models.CharField(max_length=250, blank=True, null=True)
    account_open_date = models.CharField(max_length=15, blank=True, null=True)
    location =  models.CharField(max_length=250, blank=True, null=True)
    transaction = models.IntegerField(blank=True, null=True, default=0)
    transaction_status = models.CharField(max_length=15, blank=True, null=True)
    gender = models.CharField(max_length=15, blank=True, null=True)
    
    def __str__(self):
        return self.user.username