"""
Definición de modelos de Niveles, para valuacion con base en
niveles de factores

Modelos
-------
- Nivel
"""
from .factor_models import Factor
from .puesto_models import Puesto
from .parametrovp_models import ParametroVP
from django.db import models


class Nivel(models.Model):
    """
    Modelo para Niveles de cada Factor
    """
    nivel_multiplicador = models.PositiveSmallIntegerField(default=1)
    nivel = models.CharField(max_length=200)
    factor = models.ForeignKey(
        Factor, on_delete=models.CASCADE, related_name='niveles')
    puestos = models.ManyToManyField(Puesto, through='Ponderacion')

    class Meta:
        ordering = ['nivel_multiplicador']
        unique_together = [
            ['factor', 'nivel']
        ]

    def __str__(self):
        return self.nivel

    @property
    def ponderacion(self) -> float:
        if 0 >= self.nivel_multiplicador:
            return 0
        elif 1 == self.nivel_multiplicador:
            return self.factor.ponderacion_nivel_1
        else:
            return self.factor.ponderacion_nivel_1 * (
                    self.factor.exponente ** (self.nivel_multiplicador - 1))

    @property
    def ponderacion_en_pesos(self) -> float:
        vp = ParametroVP.objects.get(parametro='ValorPunto').valor
        print(f"Nivel :: {vp =}")
        return self.ponderacion * vp
