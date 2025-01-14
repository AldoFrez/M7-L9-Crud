from django.shortcuts import render, get_object_or_404, redirect #404 es cuando tenemos un llamado a un BBDD y si no existe la info, devuelve un 404 (not found)
from .models import Link #, redirect: en caso que unaaaccio se genere existosamente, la persoan es redirigida a otra parte
from .forms import LinkForm # reforzamos el crud completo, debo tener una vista que lea

def link_list(request): # genera accion del read, hace llamado a la tabla y busqye todos los objetos y que lso traiga
    links = Link.objects.all()
    return render(request, 'app/link_list.html', {'links': links})

def link_create(request): # si hay un metodo request que sea igual a post, se ejecuta accion: vamos a conectar linkform (formulario) con el metodo requestpost y que se envie la info, se guarda en la variable form y se ejecuta una validacion
    if request.method == "POST":
        form = LinkForm(request.POST)
        if form.is_valid():
            form.save() # recien si se guarda, nos tira a la url de abajo
            return redirect('link_list') # aca esta el redirect importado
    else: # y si no son los parametros que cumplem, la variable form vale igual per ose guarda vacia, ,no va a linkform
        form = LinkForm()
    return render(request, 'app/link_form.html', {'form': form})

def link_update(request, pk): # para actualizar un elemento, tengo que ir a la casilla especifica para sobreescribir ( com oen excel) , se debe hacer mediante la identificacio nde la casilla 
    link = get_object_or_404(Link, pk=pk) # la accion se reconoce con una PK,  en djngo se crea el ID automatico, en BBDD cuando havcemos consulta, nos envia toda la info, pero soy yo quien decide en htlm que quiero mostrar (pasan todos los atributos de ese objeto) el objeto tiene igual una PK pero no esta mapeada en el html
    if request.method == "POST": # toma la BBDD, toma una PK, que pasacom oparametro de la funcion link_update, y la valida
        form = LinkForm(request.POST, instance=link) # form y linkform, vamos al formulario, y hacemos requestpost, pero revisamos la instancia que sea igual a link, cuando pasamso al formulario, ya estan cargados los valores del formularion
        if form.is_valid(): # get object, esp para obtener
            form.save()
            return redirect('link_list') # se devuelve a esta pagina
    else:
        form = LinkForm(instance=link) # nos manda lo la funcion 404
    return render(request, 'app/link_form.html', {'form': form})

def link_delete(request, pk): # generamos un proceso de flujo normal, si el usuario con ID1 existe, puedo eliminar
    link = get_object_or_404(Link, pk=pk)
    if request.method == "POST":
        link.delete()
        return redirect('link_list')
    return render(request, 'app/link_confirm_delete.html', {'link': link}) # html de confirmacion de borrado

# Create your views here.
