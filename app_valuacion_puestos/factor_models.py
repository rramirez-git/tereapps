"""
Definición de modelos de Factores

Modelos
-------
- Factor
"""
from django.db import models


def get_next_posicion_factor() -> int:
    max = Factor.objects.aggregate(models.Max('posicion'))
    try:
        return max['posicion__max'] + 1
    except TypeError:
        return 1


class Factor(models.Model):
    """
    Modelo de Factores, para ponderar los puestos
    """
    factor = models.CharField(max_length=200, unique=True)
    posicion = models.PositiveSmallIntegerField(default=get_next_posicion_factor)
    ponderacion_nivel_1 = models.DecimalField(
        max_digits=6, decimal_places=2, verbose_name="Ponderación")
    exponente = models.DecimalField(max_digits=8, decimal_places=5, default=2.1)

    class Meta:
        ordering = ['posicion', 'factor']

    def __str__(self):
        return f"{self.posicion} - {self.factor}"

    @property
    def cantidad_de_niveles(self) -> int:
        return self.niveles.all().count()
