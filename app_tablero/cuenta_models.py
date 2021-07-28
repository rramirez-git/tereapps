"""
Definición de modelos de cuentas
"""
from django.db import models

from .tablero_models import Tablero

class Cuenta(models.Model):
    nivel = models.PositiveSmallIntegerField(default=0)
    entidad = models.CharField(max_length=2)
    cuenta = models.CharField(max_length=10)
    descripcion = models.CharField(max_length=50)
    formato = models.CharField(max_length=10)

    tablero = models.ForeignKey(
        Tablero,
        on_delete=models.CASCADE,
        related_name='cuentas')

    pre_cve = models.CharField(max_length=30)
    pre_posicion = models.PositiveSmallIntegerField(default=0)
    pre_cve_2 = models.CharField(max_length=30)

    class Meta:
        ordering = ['cuenta', 'formato']

    def __str__(self):
        return f"{self.cuenta}: {self.descripcion}"
