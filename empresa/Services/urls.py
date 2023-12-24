#Se tiene que crear un archivo de urls para poder verificar donde es que se encuentran las urls
from django.urls import path 
from . import views as services_views

urlpatterns = [
    path(' ', services_views.services,name="services"),
] 