from django.urls import path

from DjangoExamPrep3.common import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='home')
]