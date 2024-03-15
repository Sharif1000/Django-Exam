from django.urls import path
from . import views

urlpatterns = [
    # path('', views.add_album, name = 'add_album'),
    path('', views.AddAlbumView.as_view(), name = 'add_album'),
    # path('edit/<int:id>', views.edit_album, name = 'edit_album'),
    path('edit/<int:pk>', views.EditAlbumView.as_view(), name = 'edit_album'),
    #path('delete/<int:id>', views.delete_album, name = 'delete_album'),
    path('delete/<int:pk>', views.DeleteAlbumView.as_view(), name = 'delete_album'),
]