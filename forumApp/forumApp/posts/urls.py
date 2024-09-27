from django.urls import path, include

from forumApp.posts import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add-book/', views.add_book, name='add-book'),
    path('<int:pk>/', include([
        path('delete-book/', views.delete_book, name='delete-book'),
    ]))
]