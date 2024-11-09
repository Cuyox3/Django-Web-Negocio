from django.db import models
from django.utils import timezone #*Puede ser from django.utils.timezone import now 
from django.contrib.auth.models import User #Importa los usuarios que podran hacer publicaciones en elblog 

# Create your models here.
class Category(models.Model):
    name =  models.CharField(max_length=100,verbose_name="Nombre")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")
 
    class Meta:
        verbose_name = "categoria"
        verbose_name_plural = "categorias"
        ordering = ["-created"]

    def __str__(self):
        return self.name
    
class Post(models.Model):
    title = models.CharField(max_length=200,verbose_name="Titulo")
    content = models.TextField(verbose_name="Contenido")
    published = models.DateField(verbose_name="Fecha de publicacion", default = timezone.now )#*Y aqui nada mas seria "now"
    image = models.ImageField(verbose_name="Imagen", upload_to="blog", null=True, blank=True)
    author = models.ForeignKey(User,verbose_name="Autor",on_delete=models.CASCADE) #Si se borra el autor se borraran sus publicaciones, se tiene que ver la documentacion para saber que es lo que se debe hacer 
    categories = models.ManyToManyField(Category, verbose_name="Categorías", related_name="get_posts")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        ordering = ["-created"]

    def __str__(self):
        return self.title