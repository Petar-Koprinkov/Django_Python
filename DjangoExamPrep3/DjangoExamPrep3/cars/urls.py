from django.urls import path, include

from DjangoExamPrep3.cars import views

urlpatterns = [
    path('create/', views.CreateCarView.as_view(), name='create-car'),
    path('catalogue/', views.CatalogueView.as_view(), name='catalogue'),
    path('<int:id>/', include([
        path('details/', views.DetailCarView.as_view(), name='details-car'),
        path('edit/', views.EditCarView.as_view(), name='edit-car'),
        path('delete/', views.DeleteCarView.as_view(), name='delete-car'),
    ])),
]