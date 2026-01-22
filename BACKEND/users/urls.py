from django.urls import path
from .views import ProfileView
from .views import LeaderboardView

urlpatterns = [
    path('profile/', ProfileView.as_view(), name='profile'),
    path('leaderboard/', LeaderboardView.as_view(), name='leaderboard'),
    ]