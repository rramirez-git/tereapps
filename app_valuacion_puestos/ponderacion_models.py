"""
Definición de modelos de Ponderacion, entre Puestos y Niveles de Factores

Modelos
-------
- Ponderacion
"""
from .nivel_models import Nivel
from .puesto_models import Puesto
from django.db import models


class Ponderacion(models.Model):
    """
    Modelo de Ponderación, para ponderar los Puestos con base ne los
    diferentes factores
    """
    puesto = models.ForeignKey(
        Puesto, on_delete=models.CASCADE, related_name="niveles_ponderacion")
    nivel = models.ForeignKey(
        Nivel, on_delete=models.CASCADE, related_name='puestos_ponderacion')

    def __str__(self):
        return f"{self.ponderacion:0.2f}"

    @property
    def ponderacion(self) -> float:
        return self.nivel.ponderacion

    @property
    def ponderacion_en_pesos(self) -> float:
        return self.nivel.ponderacion_en_pesos
