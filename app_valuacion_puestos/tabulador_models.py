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

    __cantidad_de_niveles__ = None

    @property
    def cantidad_de_niveles(self) -> int:
        if not self.__cantidad_de_niveles__:
            self.__cantidad_de_niveles__ = self.niveles.all().count()
        return self.__cantidad_de_niveles__
