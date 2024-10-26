from django.urls import path, include

from DjangoExamPrep3.cars import views

urlpatterns = [
    path('create/', views.CreateCarView.as_view(), name='create-car'),
    path('catalogue/', views.CatalogueView.as_view(), name='catalogue'),
    path('<int:id>/', include([
        path('details/', views.DetailCarView.as_view(), name='details-car'),
    ])),
]