"""
Definición de modelos de Puesto

Modelos
-------
- Puesto
"""
import decimal

from django.db import models

from .tabulador_models import Tabulador
from .parametrovp_models import ParametroVP

def get_next_posicion_puesto() -> int:
    max = Puesto.objects.aggregate(models.Max('posicion'))
    try:
        return max['posicion__max'] + 1
    except TypeError:
        return 1


class Puesto(models.Model):
    """
    Modelo de Puestos
    """
    puesto = models.CharField(max_length=200, unique=True)
    posicion = models.PositiveSmallIntegerField(
        default=get_next_posicion_puesto)
    estatus = models.BooleanField(default=True)
    tabulador = models.ForeignKey(
        Tabulador, on_delete=models.PROTECT, related_name="+")

    class Meta:
        ordering = ['posicion', 'puesto']

    def __str__(self):
        return self.puesto

    @property
    def ponderacion_total(self) -> float:
        total = decimal.Decimal(0.0)
        for nivel in self.niveles_ponderacion.all():
            total += nivel.ponderacion
        return total

    @property
    def ponderacion_total_en_pesos(self) -> float:
        vp = ParametroVP.objects.get(parametro='ValorPunto').valor
        return self.ponderacion_total * vp
