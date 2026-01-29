import profile
from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny

from django.utils import timezone
from django.db.models import Sum
from datetime import timedelta

from .serializers import RegisterSerializer

from .models import Profile, XPTransaction
from.serializers import LeaderboardSerializer, ProfileSerializer


# Create your views here.
class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response({
            "id": user.id,
            "username": user.username,
            "email": user.email,
        })
    
    def put(self, request):
        profile = Profile.objects.first()
        serializer =ProfileSerializer(profile, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class LeaderboardView(ListAPIView):
    queryset = Profile.objects.select_related('user').order_by('-xp')
    serializer_class = LeaderboardSerializer
    permission_classes = [AllowAny]
    
#All time leaderboard
class AllTimeLeaderboardView(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = LeaderboardSerializer

    def get_queryset(self):
        return Profile.objects.select_related('user').order_by('-xp')
    
    def list(self,request, *args, **kwargs):
        queryset = self.get_queryset()
        data =[]

        for index, Profile in enumerate(queryset,start=1):
            data.append({
                'rank': index,
                'username': profile.username,
                'xp': profile.xp,
                'streak': profile.streak
            })
        return Response(data)
    
#Weekly Leaderboard
class WeeklyLeaderboardView(ListAPIView):
    permission_classes = [AllowAny]

def get_queryset(self):
        return Profile.objects.select_related('user').order_by('-xp')

def list(self, request, *args, **kwargs):
    one_week_ago = timezone.now() - timedelta(days=7)

    weekly_xp =(
        XPTransaction.objects.filter(created_at__gte=one_week_ago).
        values('user__username').annotate(total_xp=Sum('amount')).order_by('-total_xp')    
    )
    data = []
    for index, entry in enumerate(weekly_xp, start=1):
        data.append({
            'rank': index,
            'username': entry['user__username'],
            'xp': entry['total_xp'] or 0,
        })
    return Response(data)

class RegisterView(APIView):
    permission_classes = []

    def post(self, request):
        user = User.objects.create_user(
            username=request.data['username'],
            password=request.data['password']
        )
        return Response({"message": "User created"})
