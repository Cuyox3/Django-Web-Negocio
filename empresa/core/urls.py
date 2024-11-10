from django.urls import path 
from . import views as core_views

urlpatterns = [
    path('about/', core_views.about,name="about"),
    path('contact/', core_views.contact,name="contact"),
    path('', core_views.home,name="home"), #No lleva /home por que es la pagina principal
    path('store/', core_views.store, name="store"),

]