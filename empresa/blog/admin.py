from django.contrib import admin
from .models import Category, Post
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class PostAdmin(admin.ModelAdmin): 
    readonly_fields = ('created', 'updated')
    list_display = ('title', 'author', 'published','post_categories') #Hace columnas para ver mas iformacion 
    ordening = ('author', ' published') #Permite hacer filtros, tiene que tener una coma para saber que es una tupla
    search_fields = ('title', 'content', 'author__username','categories')#Para autor tiene que tener dos barras bajas para poder hacer la busqueda por usuario
    date_hierarchy = 'published'  #Te da jerarquia para verificar las fechas 
    list_filter = ('author__username','categories__name')#categories es un campo m2m 

    def post_categories(self, obj): 
        return ",".join([c.name for c in obj.categories.all().order_by("name")])#genera cadena de caracteres separadas por comas
    post_categories.short_description = "Categorias" #Se le puede agregar HTML


admin.site.register(Category,CategoryAdmin)
admin.site.register(Post, PostAdmin)