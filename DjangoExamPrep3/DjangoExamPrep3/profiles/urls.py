from django.urls import path

from DjangoExamPrep3.profiles import views

urlpatterns = [
    path('create/', views.CreateProfileView.as_view(), name='create-profile'),
    path('details/', views.DetailsProfileView.as_view(), name='details-profile'),
    path('edit/', views.EditProfileView.as_view(), name='edit-profile'),
]