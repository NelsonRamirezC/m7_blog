from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, null=False, blank=False, unique=True)
    descripcion = models.TextField(null=False, blank=False)


    def __str__(self):
        return self.nombre
    
    class Meta:
        managed = True
        db_table = 'categorias'
    

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=50, null=False, blank=False)
    contenido = models.TextField(null=False, blank=False)
    fecha_creacion = models.DateField(auto_created=True, auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=False, blank=False, default=4)


    def __str__(self):
        return self.titulo
    
    class Meta:
        managed = True
        db_table = 'posts'