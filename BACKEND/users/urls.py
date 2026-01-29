from django.urls import path
from .views import AllTimeLeaderboardView, ProfileView, WeeklyLeaderboardView, RegisterView
from .views import LeaderboardView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_simplejwt.views import TokenBlacklistView

urlpatterns = [
    path('profile/', ProfileView.as_view(), name='profile'),
    path('leaderboard/', LeaderboardView.as_view(), name='leaderboard'),
    path('leaderboard/all-time/', AllTimeLeaderboardView.as_view(), name='all_time_leaderboard'),
    path('leaderboard/weekly/', WeeklyLeaderboardView.as_view(), name='weekly_leaderboard'),
    path('register/', RegisterView.as_view(),name='register'),
    path('auth/login/', TokenObtainPairView.as_view(), name='login'),
    path('auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/logout/', TokenBlacklistView.as_view(), name='logout'),
]