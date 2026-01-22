from rest_framework import serializers
from .models import Profile

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
        