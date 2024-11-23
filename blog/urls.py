from django.urls import path

from . import views

urlpatterns = [
    path('', views.posts, name="posts"),
    path('post/add/', views.crear_post, name="crear_post"),
]
