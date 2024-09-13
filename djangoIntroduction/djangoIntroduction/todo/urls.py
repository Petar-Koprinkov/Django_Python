from django.urls import path

from djangoIntroduction.todo.views import index

urlpatterns = [
    path('', index, name='index'),
]