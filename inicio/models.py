from django.db import models

class Manga(models.Model):
    nombre = models.CharField(max_length=30)
    autor = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=100)
    anio = models.IntegerField()
    tipo = 'manga'

    def __str__(self):
        return f'{self.nombre} - {self.autor} - {self.tipo}'