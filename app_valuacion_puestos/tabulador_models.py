"""
Definición de modelos de Tabuladores

Modelos
-------
- Tabulador
"""
from django.db import models


class Tabulador(models.Model):
    """
    Modelo de Tabulador
    """
    tabulador = models.CharField(max_length=200, unique=True)

    class Meta:
        ordering = ['tabulador']

    def __str__(self):
        return self.tabulador

    @property
    def cantidad_de_niveles(self) -> int:
        return self.niveles.all().count()
