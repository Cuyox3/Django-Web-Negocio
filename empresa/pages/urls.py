from django.urls import path 
from .import views 

urlpatterns = [
    path('<int:page_id>/', views.page, name="page"),#con el int: solo se cambia no se castea
    #Lo que est een medio de <> es un tipo dinamico ys on cadenas de caracteres
]
 
