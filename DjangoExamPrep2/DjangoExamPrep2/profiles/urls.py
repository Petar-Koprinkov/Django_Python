from django.urls import path

from DjangoExamPrep2.profiles import views

urlpatterns = [
    path('create/', views.CreateProfileView.as_view(), name='create_profile'),
    path('details/', views.DetailsProfileView.as_view(), name='details_profile'),
]