from rest_framework import serializers
from .models import Profile
from django.contrib.auth.models import User

class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    email = serializers.EmailField(source = 'user.email', read_only=True)

    class Meta:
        model = Profile
        fields = [
            'id',
            'username',
            'email',
            'xp',
            'streak',
            'created_at',
        ]

class LeaderboardSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source = 'user.username')
    rank= serializers.IntegerField(read_only = True)

    class Meta:
        model = Profile
        fields = ['rank','username','xp','streak']
        
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True)
    password2 = serializers.CharField(write_only = True)

    class Meta:
        model = User
        fields =('username', 'email', 'password','password2')

        def validate (self, attrs):
            if attrs['password']!=attrs['password2']:
                raise serializers.ValidationError("Passwords do not match")
            return attrs
        
        def create(self, validated_data):
            validated_data.pop('password2')

            user = User.objects.create_user(
                username=validated_data['username'],
                email=validated_data.get('email'),
                password=validated_data['password']
            )
            return user
