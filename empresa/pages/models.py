from django.db import models

# Create your models here.
class Pages(models.Model):
    title  = models.TextField(verbose_name="Titulo", max_length=100, unique=True) # HEcha para
    content = models.TextField(verbose_name="Contenido")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Pagina"
        verbose_name_plural = "Paginas"
        ordering = ["title"]

    def __str__(self):
        return self.title

