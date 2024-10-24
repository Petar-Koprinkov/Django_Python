from django.urls import path

from DjangoExamPrep2.common import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('catalogue/', views.CatalogPageView.as_view(), name='catalogue'),

]