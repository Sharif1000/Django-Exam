
from django.urls import path
from .views import UserRegistrationView, UserLoginView, UserLogoutView, UserBankAccountUpdateView, ChangePasswordView

from . import views

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    # path('logout/', UserLogoutView.as_view(), name='logout'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/', UserBankAccountUpdateView.as_view(), name='profile'),
    # path('changepass/', views.changepass, name='changepass'),
    path('changepass/', ChangePasswordView.as_view(), name='changepass'),
]