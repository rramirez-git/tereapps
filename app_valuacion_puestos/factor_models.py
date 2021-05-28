"""
Definición de modelos de Factores

Modelos
-------
- Factor
"""
from django.db import models

from .parametrovp_models import ParametroVP


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
    posicion = models.PositiveSmallIntegerField(
        default=get_next_posicion_factor)
    ponderacion_nivel_1 = models.DecimalField(
        max_digits=6, decimal_places=2, verbose_name="%")

    class Meta:
        ordering = ['posicion', 'factor']

    def __str__(self):
        return f"{self.posicion} - {self.factor}"

    __cantidad_de_niveles__ = None
    __exponente__ = None
    __min_nivel__ = None
    __max_nivel__ = None

    @property
    def cantidad_de_niveles(self) -> int:
        if not self.__cantidad_de_niveles__:
            self.__cantidad_de_niveles__ = self.niveles.all().count()
        return self.__cantidad_de_niveles__

    @property
    def exponente(self):
        if not self.__exponente__:
            self.__exponente__ = ParametroVP.objects.get(
                parametro=f"Exponente{self.cantidad_de_niveles}N").valor
        return self.__exponente__

    @property
    def min_nivel(self):
        if not self.__min_nivel__:
            self.__min_nivel__ = self.niveles.order_by('nivel_multiplicador')[0]
        return  self.__min_nivel__

    @property
    def max_nivel(self):
        if not self.__max_nivel__:
            self.__max_nivel__ = self.niveles.order_by('-nivel_multiplicador')[0]
        return self.__max_nivel__

    def as_dict(self):
        return {
            'id': self.pk,
            'factor': self.factor,
            'posicion': self.posicion,
            'ponderacion_nivel_1': float(self.ponderacion_nivel_1),
            'cantidad_de_niveles': self.cantidad_de_niveles,
            'exponente': float(self.exponente),
            'min_nivel': self.min_nivel.as_dict(),
            'max_nivel': self.max_nivel.as_dict(),
            'niveles': [nivel.as_dict() for nivel in self.niveles.all()],
        }
