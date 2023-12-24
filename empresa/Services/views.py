from django.shortcuts import render
from .models import Service

# Create your views here.
def services(request):
    servicios = Service.objects.all()  #Servicios es la lista de los modelos
    return render(request, "services/services.html", {'services' : servicios})  #Services es la variable que se va a recorrer al momento de verificar la base de datos
