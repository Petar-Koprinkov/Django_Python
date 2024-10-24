from django.urls import path

from DjangoExamPrep2.profiles import views

urlpatterns = [
    path('create/', views.CreateProfileView.as_view(), name='create_profile'),
]