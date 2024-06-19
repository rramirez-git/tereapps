"""
Definición de modelos de Niveles, para valuacion con base en
niveles de factores

Modelos
-------
- Nivel
"""
from .factor_models import Factor
from .parametrovp_models import ParametroVP
from .puesto_models import Puesto
from django.db import models
from zend_django.models import ParametroSistema


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

    __ponderacion__ = None
    __ponderacion_en_pesos__ = None

    @property
    def ponderacion(self) -> float:
        if not self.__ponderacion__:
            if 0 >= self.nivel_multiplicador:
                self.__ponderacion__ = 0
            elif 1 == self.nivel_multiplicador:
                self.__ponderacion__ = float(self.factor.ponderacion_nivel_1)
            else:
                self.__ponderacion__ = float(
                    self.factor.ponderacion_nivel_1) * (
                        self.factor.exponente ** (
                            self.nivel_multiplicador - 1))
        return self.__ponderacion__

    @property
    def ponderacion_en_pesos(self) -> float:
        if not self.__ponderacion_en_pesos__:
            dias = float(ParametroSistema.get(
                'AppValuacionPuestos', 'DiasPorMes'))
            vp = float(ParametroVP.objects.get(parametro='ValorPunto').valor)
            self.__ponderacion_en_pesos__ = self.ponderacion * vp * dias
        return self.__ponderacion_en_pesos__

    def as_dict(self):
        return {
            'id': self.pk,
            'nivel_multiplicador': self.nivel_multiplicador,
            'nivel': self.nivel,
            'ponderacion': float(self.ponderacion),
            'ponderacion_en_pesos': float(self.ponderacion_en_pesos),
        }
