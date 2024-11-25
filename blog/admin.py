from django.contrib import admin
from .models import Post, Categoria, Comentario

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo')
    search_fields = ('titulo',)
    list_filter = ('categoria',)
    

admin.site.register(Post, PostAdmin)


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    search_fields = ('nombre',)
    list_filter = ('nombre',)
    

admin.site.register(Categoria, CategoriaAdmin)


class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'contenido', 'fecha')
    search_fields = ('contenido',)
    list_filter = ('autor', 'fecha')
    

admin.site.register(Comentario, ComentarioAdmin)