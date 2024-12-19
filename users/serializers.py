from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id' , 'profile_pic', 'bio', 'designation','status','phone_number','account_name','account_open_date','location','transaction','transaction_status','gender']

class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = ['id', "username", 'first_name', 'last_name', 'email', 'profile']

    def create(self, validated_data):
        # Extract nested profile data
        profile_data = validated_data.pop('profile', {})
        password = validated_data.pop('password', None)

        # Create the user
        user = User(**validated_data)
        if password:
            user.set_password(password)
        user.save()

        # Create the associated profile
        Profile.objects.create(user=user, **profile_data)

        return user

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile', {})
        profile = instance.profile

        instance.first_name = validated_data.get('first_name', instance.first_name) 
        instance.last_name = validated_data.get('last_name', instance.last_name)  
        instance.email = validated_data.get('email', instance.email)
        instance.save()

        profile.profile_pic = profile_data.get('profile_pic', profile.profile_pic)
        profile.bio = profile_data.get('bio', profile.bio)
        profile.phone_number = profile_data.get('phone_number', profile.phone_number)
        profile.account_name = profile_data.get('account_name', profile.account_name)
        profile.account_open_date = profile_data.get('account_open_date', profile.account_open_date)
        profile.location = profile_data.get('location', profile.location)
        profile.transaction = profile_data.get('transaction', profile.transaction)
        profile.transaction_status = profile_data.get('transaction_status', profile.transaction_status)
        profile.gender = profile_data.get('gender', profile.gender)
        profile.save()

        return instance
