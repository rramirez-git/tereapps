"""
Definición de modelos de Niveles de Tabulador

Modelos
-------
- TabuladorNivel
"""
from .tabulador_models import Tabulador
from django.db import models


class TabuladorNivel(models.Model):
    """
    Modelo para Niveles de cada Tabulador
    """
    posicion = models.PositiveSmallIntegerField(default=1)
    porcentaje = models.DecimalField(max_digits=6, decimal_places=2)
    tabulador = models.ForeignKey(
        Tabulador, on_delete=models.CASCADE, related_name='niveles')

    class Meta:
        ordering = ['tabulador', 'posicion']
        unique_together = [
            ['tabulador', 'posicion']
        ]

    def __str__(self):
        return f"{self.posicion}: {self.porcentaje}%"
