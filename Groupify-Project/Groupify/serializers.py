from rest_framework import serializers
from .models import User, Group

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'firstName', 'lastName')

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'title', 'description', 'visibility', 'category', 'creator', 'admins', 'users', 'members')