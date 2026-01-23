from django.urls import path
from .views import AllTimeLeaderboardView, ProfileView, WeeklyLeaderboardView, RegisterView
from .views import LeaderboardView

urlpatterns = [
    path('profile/', ProfileView.as_view(), name='profile'),
    path('leaderboard/', LeaderboardView.as_view(), name='leaderboard'),
    path('leaderboard/all-time/', AllTimeLeaderboardView.as_view(), name='all_time_leaderboard'),
    path('leaderboard/weekly/', WeeklyLeaderboardView.as_view(), name='weekly_leaderboard'),
    path('register/', RegisterView.as_view(),name='register'),
]