from django.urls import path, include

from DjangoBasicExam.posts import views

urlpatterns = [
    path('create/', views.CreatePostView.as_view(), name='create-post'),
    path('<int:post_id>/', include([
        path('details/', views.DetailsPostView.as_view(), name='details-post'),
    ])),
]