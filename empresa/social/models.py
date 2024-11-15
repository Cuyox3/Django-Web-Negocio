from django.db import models

# Create your models here.
class Link(models.Model):
    key  = models.SlugField(verbose_name="Nombre clave", max_length=100, unique=True) # HEcha para
    name = models.CharField(verbose_name="Nombre", max_length=100)
    url = models.URLField(verbose_name="Link",null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Enlace"
        verbose_name_plural = "Enlaces"
        ordering = ["name"]

    def __str__(self):
        return self.name
