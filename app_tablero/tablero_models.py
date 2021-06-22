"""
Definición de modelos para Tableros
"""
from django.db import models

class Tablero(models.Model):
    nombre = models.CharField(max_length=50)

    class Meta:
        ordering = ['nombre']

    def __str__(self):
        return self.nombre
