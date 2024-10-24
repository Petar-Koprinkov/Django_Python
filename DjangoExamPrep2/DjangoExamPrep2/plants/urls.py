from django.urls import path

from DjangoExamPrep2.plants import views

urlpatterns = [
    path('create/', views.CreatePlantView.as_view(), name='create-plant'),
    path('details/<int:plant_id>', views.DetailsPlantView.as_view(), name='details-plant'),
    path('edit/<int:plant_id>', views.EditPlantView.as_view(), name='edit-plant'),
    path('delete/<int:plant_id>', views.DeletePlantView.as_view(), name='delete-plant'),
]