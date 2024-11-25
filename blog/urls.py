from django.urls import path

from . import views

urlpatterns = [
    path('', views.posts, name="posts"),
    path('post/add/', views.crear_post, name="crear_post"),
    path('post/detalle/<int:post_id>', views.detalle_post, name="detalle_post"),
]
