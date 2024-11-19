from django.urls import path
from rest_framework_simplejwt.views import  TokenRefreshView
from . import views
urlpatterns = [
    path('login/', views.CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', views.RegisterUserView.as_view(), name='register_user'),
]
