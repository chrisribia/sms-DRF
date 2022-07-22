from djoser.serializers import UserCreateSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model 
User = get_user_model()

class UserCreateSerializer(UserCreateSerializer):
    class Meta:
        model = User
        fields = ('id','email','name','password')



 