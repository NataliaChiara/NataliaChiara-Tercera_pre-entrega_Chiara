from django import forms

class CrearMangaFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    autor = forms.CharField(max_length=30)
    descripcion = forms.CharField(max_length=100)
    anio = forms.IntegerField()

class BusquedaMangaFormulario(forms.Form):
    nombre = forms.CharField(max_length=30, required=False)

class CrearMaquillajeFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    marca = forms.CharField(max_length=30)