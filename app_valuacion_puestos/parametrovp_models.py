"""
Definición de modelos de Parametros

Modelos
-------
- ParametroVP
- ParametroVPHistoria
"""
from datetime import date
from django.db import models

from zend_django.templatetags.utils import GetNextPrevObject


class ParametroVP(models.Model):
    """
    Modelo de Parámetros, para la aplicacion
    """
    parametro = models.CharField(max_length=200)
    valor = models.DecimalField(max_digits=8, decimal_places=5)
    fecha = models.DateField(default=date.today)

    class Meta:
        ordering = ['parametro', 'fecha']

    def __str__(self):
        return self.parametro

    def save(self, *args, **kwargs):
        self.fecha = date.today()
        super(ParametroVP, self).save(*args, **kwargs)
        ParametroVPHistoria.objects.create(
            raiz=self,
            parametro=self.parametro,
            valor=self.valor
        )


class ParametroVPHistoria(models.Model):
    """
    Modelo para almacenar la historia de los valores de un parámetro
    """
    raiz = models.ForeignKey(
        ParametroVP, on_delete=models.CASCADE, related_name="historia")
    parametro = models.CharField(max_length=200)
    valor = models.DecimalField(max_digits=8, decimal_places=5)
    fecha = models.DateField(default=date.today)

    class Meta:
        ordering = ['raiz', '-fecha', '-pk']

    def __str__(self):
        return f"{self.raiz}"

    @property
    def cambio_porcentual(self):
        obj = GetNextPrevObject(self, False, self.__class__.objects.filter(
            raiz=self.raiz))
        if obj:
            return (self.valor - obj.valor) / obj.valor * 100
        return 0.0
