"""
Definición de modelos para Estadisticos de cuentas
"""
from django.db import models
from datetime import date

from .cuenta_models import Cuenta


def get_4_month(fecha) -> date:
    return date(fecha.year, fecha.month, 1)


def get4month() -> date:
    return get_4_month(date.today())

class Estadistico(models.Model):
    periodo = models.DateField(default=get4month)
    cantidad = models.DecimalField(max_digits=12, decimal_places=2)

    cuenta = models.ForeignKey(
        Cuenta,
        related_name='detalle',
        on_delete=models.PROTECT)

    class Meta:
        ordering = ['cuenta', '-periodo']

    def __str__(self):
        return f"{self.cantidad}"
