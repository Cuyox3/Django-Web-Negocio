from django.shortcuts import render, get_object_or_404
from .models import Post,Category#Se tienen que agregar todas las apps para poder mostrarlas dentro del html
# Create your views here.

def blog(request): 
    posts = Post.objects.all()
    return render(request, "blog/blog.html", {'posts':posts}) #Aqui se tiene que especificar la ubicacion del archivo 
#Por que se tiene que meter dentro de una carpeta un archivo html en template? 
#El diccionario tiene que tener el mismo nombre que la clave para podere recorrerlo en el for del html 


#def category (request, category_id):
#    category = get_object_or_404(Category, id=category_id)
#    return render (request, "blog/category.html", {'category':category})




def category (request, category_id):
    category = get_object_or_404(Category,id=category_id)
    posts  = Post.objects.filter  (categories=category)
    return render (request, "blog/category.html", {'category':category,
                                                  'posts':posts})