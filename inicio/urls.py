
from django.urls import path
from inicio.views import inicio, mangas, crear_manga

urlpatterns = [
    path('', inicio, name='inicio'),
    path('mangas/', mangas, name='mangas'),
    path('mangas/crear/', crear_manga, name='crear_manga')
]
