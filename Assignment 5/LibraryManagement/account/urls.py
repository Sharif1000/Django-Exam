
from django.urls import path
from .views import UserRegistrationView, UserLoginView
from . import views

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', views.user_logout, name='logout'),
    path("deposit/", views.deposite, name="deposit_money"),
    path("profile/", views.profile, name="profile"),
]