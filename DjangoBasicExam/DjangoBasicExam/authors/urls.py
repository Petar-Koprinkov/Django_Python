from django.urls import path

from DjangoBasicExam.authors import views

urlpatterns = [
    path('create/', views.CreateAuthorView.as_view(), name='create-author'),
]