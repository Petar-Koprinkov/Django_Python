from django.urls import path, include

from DjangoExamPrep.albums import views

urlpatterns = [
    path('add/', views.AddAlbumView.as_view(), name='add-album'),
    path('<int:id>/', include([
        path('edit/', views.EditAlbumView.as_view(), name='edit-album'),
        path('details/', views.DetailAlbumView.as_view(), name='details-album'),
        path('delete/', views.DeleteAlbumView.as_view(), name='delete-album'),
    ]))
]