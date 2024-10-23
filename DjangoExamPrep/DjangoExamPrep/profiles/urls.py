from django.urls import path

from DjangoExamPrep.profiles import views

urlpatterns = [
    path('details/', views.DetailProfileView.as_view(), name='detail-profile'),
    path('delete/', views.DeleteProfileView.as_view(), name='delete-profile'),
]