from django.contrib import admin
from .models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number', 'bio', "transaction",'account_open_date', 'profile_pic')  # Columns to display in the admin list view
    search_fields = ('user__username', 'phone_number')  # Search by user and phone number
    list_editable = ('transaction','account_open_date','profile_pic')