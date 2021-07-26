from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.Post.as_view()),
    path('', views.Index.as_view()),
]