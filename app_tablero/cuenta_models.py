"""
Definición de modelos de cuentas
"""
import json

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

    __cuentas_hijo = list()
    __periodos_total = list()
    __periodos_promedio = list()

    class Meta:
        ordering = ['cuenta', 'formato']

    def __str__(self):
        return f"{self.cuenta}: {self.descripcion}"

    @property
    def cuentas_hijo(self):
        if len(self.__cuentas_hijo) == 0:
            self.__cuentas_hijo = list(self.tablero.cuentas.filter(
                pre_cve__endswith=self.cuenta, entidad='T'))
        return self.__cuentas_hijo

    @property
    def tiene_hijos(self):
        return len(self.cuentas_hijo) > 0

    @property
    def periodos_total(self):
        if len(self.__periodos_total) == 0:
            self.__periodos_total = [
                float(reg['cantidad'])
                for reg in self.detalle.all().values('cantidad')]
        return self.__periodos_total

    @property
    def periodos_promedio(self):
        if len(self.__periodos_promedio) == 0:
            if self.tablero.cuentas.filter(
                    cuenta=self.cuenta, entidad='PT').exists():
                self.__periodos_promedio = [
                    float(reg['cantidad'])
                    for reg in self.tablero.cuentas.filter(
                        cuenta=self.cuenta, entidad='PT'
                        )[0].detalle.all().values('cantidad')]
        return self.__periodos_promedio

    @property
    def periodos_total_json(self):
        return json.dumps(self.periodos_total)

    @property
    def periodos_promedio_json(self):
        return json.dumps(self.periodos_promedio)
