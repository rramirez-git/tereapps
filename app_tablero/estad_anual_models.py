from django.db import models
from datetime import date

from zend_django.templatetags.utils import GetNextPrevObject
from .cuenta_models import Cuenta


class EstadisticoAnual(models.Model):
    anio = models.PositiveSmallIntegerField(
        default=date.today().year, verbose_name="Año")
    cantidad = models.DecimalField(max_digits=12, decimal_places=2)

    __periodo_anterior = None

    cuenta = models.ForeignKey(
        Cuenta,
        related_name='detalle_anual',
        on_delete=models.CASCADE)

    class Meta:
        ordering = ['cuenta', 'anio']

    def __str__(self):
        return f"{self.cantidad}"

    @property
    def periodo_anterior(self):
        if self.__periodo_anterior is None:
            self.__periodo_anterior = GetNextPrevObject(
                self, True, self.cuenta.detalle_anual)
        return self.__periodo_anterior

    @property
    def porc_ant(self):
        if self.periodo_anterior is not None:
            try:
                return round(float(
                    self.cantidad - self.periodo_anterior.cantidad) / float(
                    self.cantidad) * 100)
            except ZeroDivisionError:
                pass
        return 0

    @property
    def porc_vta(self):
        cta_vtas = self.cuenta.tablero.cta_vta_neta
        vtas_per_actual = cta_vtas.detalle_anual.filter(anio=self.anio)
        if vtas_per_actual.exists():
            vtas_per_actual = vtas_per_actual[0]
            return round(float(self.cantidad) / float(
                vtas_per_actual.cantidad) * 100)
        return 0
