from django.urls import path
from . import views

urlpatterns = [
    path('signup/',views.signup,name='signup'),
    path('login/',views.UserLoginView.as_view(),name='user_login'),
    path('logout/',views.user_logout,name='user_logout'),
    path('profile/',views.profile,name='profile'),
    path('profile/edit/<int:pk>/',views.EditProfileView.as_view(),name='edit_profile'),  
]
