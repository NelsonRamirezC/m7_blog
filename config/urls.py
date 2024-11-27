from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tema/<str:tema>/', views.tema, name="tema"),
    path('', views.index, name="index"),
    path('', include('usuarios.urls')),
    path('blog/', include('blog.urls')),
]
