from django.urls import path 
from .import views 

urlpatterns = [
    path('', views.blog,name="blog"), #Aqui va vacio
    path('category/<int:category_id>/', views.category, name="category"),#con el int: solo se cambia no se castea 
    #Lo que est een medio de <> es un tipo dinamico ys on cadenas de caracteres
]
 
