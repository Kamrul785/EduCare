from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer, UserSerializer as BaseUserSerializer
from rest_framework import serializers
from users.models import User

class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        model = User
        fields = ['id','first_name', 'last_name', 'email', 'password', 'role', 'address' ,'phone_number']
        extra_kwargs = {'password': {'write_only': True}}


class UserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        model = User
        fields = ['id','first_name','last_name', 'email', 'role', 'address' ,'phone_number']
            
        