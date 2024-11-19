from typing import Any, Dict
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfile
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer



"""
Extending the TokenObtainPairSerializer to add the is_admin flag
which is used in front end to route to the specific page

"""
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs: Dict[str, Any]) -> Dict[str, str]:
        data =  super().validate(attrs)
        user = self.user
        data['is_admin'] = user.is_admin
        return data



     

class RegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = ['username', 'email', 'password', 'phone_number', 'is_admin']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # Extract UserProfile data
        print(f'Data to validate: {validated_data}')
        profile_data = {
            'phone_number': validated_data.pop('phone_number', None),
            'is_admin': validated_data.pop('is_admin', None)
        }
        # Create User
        user = UserProfile.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            **profile_data
        )
        return user
