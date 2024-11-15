from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class Pages(models.Model):
    title  = models.TextField(verbose_name="Titulo", max_length=100, unique=True) # HEcha para
    content = RichTextField(verbose_name="Contenido")
    order = models.SmallIntegerField(verbose_name="Orden", default=0)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Pagina"
        verbose_name_plural = "Paginas"
        ordering = ["order","title"] #Esto va por orden de prioridad

    def __str__(self):
        return self.title

