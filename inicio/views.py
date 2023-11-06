from django.shortcuts import render, redirect
from inicio.models import Manga
from inicio.forms import CrearMangaFormulario, BusquedaMangaFormulario

def inicio(request):
    return render(request, 'inicio/inicio.html', {})

def mangas(request):
    formulario = BusquedaMangaFormulario(request.GET)
    if formulario.is_valid():
        manga_a_buscar = formulario.cleaned_data.get('nombre')
        listado_de_mangas = Manga.objects.filter(nombre__icontains = manga_a_buscar)
        
    return render(request, 'inicio/mangas.html', {'formulario': formulario, 'listado_de_mangas': listado_de_mangas}) 
    
def crear_manga(request):
    if request.method == 'POST':
        formulario = CrearMangaFormulario(request.POST)
        if formulario.is_valid():
            info_limpia = formulario.cleaned_data
            nombre = info_limpia.get('nombre')
            autor = info_limpia.get('autor')
            descripcion = info_limpia.get('descripcion')
            anio = info_limpia.get('anio')
            manga = Manga(nombre=nombre, autor=autor, descripcion=descripcion, anio=anio)
            manga.save()
            return redirect('mangas')
        else:
            return render(request, 'inicio/crear_manga.html' , {'formulario': formulario})

    formulario = CrearMangaFormulario()
    return render(request, 'inicio/crear_manga.html' , {'formulario': formulario})