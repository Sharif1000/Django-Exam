
from django.urls import path
from . import views

urlpatterns = [
    # path('', views.add_musician, name = 'add_musician'),
    path('', views.AddMusicianView.as_view(), name = 'add_musician'),
    path('signup/', views.signup, name='signup'),
    # path('login/', views.user_login, name='login'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.user_logout, name='logout'),
    # path('edit/<int:id>', views.edit_musician, name = 'edit_musician'),
    path('edit/<int:pk>', views.EditMusicianView.as_view(), name = 'edit_musician')
]