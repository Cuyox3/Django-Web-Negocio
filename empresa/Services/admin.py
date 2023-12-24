from django.contrib import admin
from .models import Service

# Register your models here.
class ServiceAdmin(admin.ModelAdmin): #Las mayusculas y minusculas importan mucho
    readonly_files = ('created', 'updated')


admin.site.register(Service, ServiceAdmin) #Es "site" sin la s 