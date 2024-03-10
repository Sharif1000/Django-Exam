from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='homepage'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('changepass/', views.changepass, name='changepass'),
    path('changepassold/', views.changepassold, name='changepassold'),
    path('profile/', views.profile, name='profile'),
]