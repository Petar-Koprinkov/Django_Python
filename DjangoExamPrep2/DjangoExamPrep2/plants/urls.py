from django.urls import path

from DjangoExamPrep2.plants import views

urlpatterns = [
    path('create/', views.CreatePlantView.as_view(), name='create-plant'),

]