from django.urls import path
from .views import accountsViews
from rest_framework_simplejwt import views

urlpatterns = [
    path("accounts/", accountsViews.as_view()),
    path("login/", views.TokenObtainPairView.as_view()),
    path("token/refresh/", views.TokenRefreshView.as_view()),
]
