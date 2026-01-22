from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny

from .models import Profile
from.serializers import LeaderboardSerializer, ProfileSerializer


# Create your views here.
class ProfileView(APIView):
    permission_classes = []

    def get(self, request):
        profile = Profile.objects.first ()
        serializer = ProfileSerializer (profile)
        return Response (serializer.data)
    
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
    