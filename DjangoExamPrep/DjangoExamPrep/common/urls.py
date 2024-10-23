from django.urls import path

from DjangoExamPrep.common import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
]