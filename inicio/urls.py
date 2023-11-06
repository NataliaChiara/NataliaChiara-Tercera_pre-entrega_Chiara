
from django.urls import path
from inicio.views import inicio, productos, crear_productos

urlpatterns = [
    path('', inicio, name='inicio'),
    path('productos/', productos, name='productos'),
    path('productos/crear/', crear_productos, name='crear_productos')
]
