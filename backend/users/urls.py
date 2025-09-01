from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RegisterView, VerifyPhoneView, ProfileView

urlpatterns = [
    path("register/", RegisterView.as_view()),
    path("verify-phone/", VerifyPhoneView.as_view()),
    path("token/", TokenObtainPairView.as_view()),
    path("token/refresh/", TokenRefreshView.as_view()),
    path("profile/", ProfileView.as_view()),
]
