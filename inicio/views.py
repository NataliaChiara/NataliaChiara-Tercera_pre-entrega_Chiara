from django.shortcuts import render, redirect
from inicio.models import Manga, Maquillaje, Comida
from inicio.forms import CrearMangaFormulario, BusquedaMangaFormulario, CrearMaquillajeFormulario, CrearComidaFormulario

def inicio(request):
    return render(request, 'inicio/inicio.html', {})

def productos(request):
    busqueda = BusquedaMangaFormulario(request.GET)
    if busqueda.is_valid():
        manga_a_buscar = busqueda.cleaned_data.get('nombre')
        listado_de_mangas = Manga.objects.filter(nombre__icontains = manga_a_buscar)
    else:
        listado_de_mangas = Manga.objects.all()

    listado_de_maquillaje = Maquillaje.objects.all()
    listado_de_comida = Comida.objects.all()
        
    return render(request, 'inicio/productos.html', {'busqueda': busqueda, 'listado_de_mangas': listado_de_mangas, 'listado_de_maquillaje': listado_de_maquillaje, 'listado_de_comida': listado_de_comida}) 
    
def crear_productos(request):
    if request.method == 'POST':
        formulario_mangas = CrearMangaFormulario(request.POST)
        if formulario_mangas.is_valid():
            info_limpia = formulario_mangas.cleaned_data
            nombre = info_limpia.get('nombre')
            autor = info_limpia.get('autor')
            descripcion = info_limpia.get('descripcion')
            anio = info_limpia.get('anio')
            manga = Manga(nombre=nombre, autor=autor, descripcion=descripcion, anio=anio)
            manga.save()
            return redirect('productos')
        
        formulario_maquillaje = CrearMaquillajeFormulario(request.POST)
        if formulario_maquillaje.is_valid():
            info_limpia = formulario_maquillaje.cleaned_data
            nombre = info_limpia.get('nombre')
            marca = info_limpia.get('marca')
            maquillaje = Maquillaje(nombre=nombre, marca=marca)
            maquillaje.save()
            return redirect('productos')
        
        formulario_comida = CrearComidaFormulario(request.POST)
        if formulario_comida.is_valid():
            info_limpia = formulario_comida.cleaned_data
            nombre = info_limpia.get('nombre')
            vencimiento = info_limpia.get('vencimiento')
            comida = Comida(nombre=nombre, vencimiento=vencimiento)
            comida.save()
            return redirect('productos')

    formulario_mangas = CrearMangaFormulario()
    formulario_maquillaje = CrearMaquillajeFormulario()
    formulario_comida = CrearComidaFormulario()
    return render(request, 'inicio/crear_productos.html' , {'formulario_mangas': formulario_mangas, 'formulario_maquillaje': formulario_maquillaje, 'formulario_comida': formulario_comida})