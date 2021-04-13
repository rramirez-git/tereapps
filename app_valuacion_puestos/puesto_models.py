"""
Definición de modelos de Puesto

Modelos
-------
- Puesto
"""
from django.db import models

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
    posicion = models.PositiveSmallIntegerField(default=get_next_posicion_puesto)
    estatus = models.BooleanField(default=True)

    class Meta:
        ordering = ['posicion', 'puesto']

    def __str__(self):
        return self.puesto

    @property
    def ponderacion_total(self) -> float:
        total = 0.0
        for factor in self.niveles_ponderacion.all():
            total += factor.ponderacion
        return total
