from django.db import models

class Manga(models.Model):
    nombre = models.CharField(max_length=30)
    autor = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=100)
    anio = models.IntegerField()

    def __str__(self):
        return f'{self.nombre} - {self.autor}'

class Maquillaje(models.Model):
    nombre = models.CharField(max_length=30)
    marca = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.nombre} - {self.marca}'
    
class Comida(models.Model):
    nombre = models.CharField(max_length=30)
    vencimiento = models.IntegerField()

    def __str__(self):
        return f'{self.nombre} - {self.vencimiento}'