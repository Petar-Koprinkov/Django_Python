from django.urls import path

from DjangoExamPrep3.profiles import views

urlpatterns = [
    path('create/', views.CreateProfileView.as_view(), name='create-profile'),
]