"""
Formularios para modelo Relacion

Formularios
-----------
frmRelacion
    Formulario completo
    - campo_izquierda
    - tipo
    - campo_derecha
"""
from django import forms

from .reporte_models import Relacion
from zend_django.hiperforms import HorizontalModelForm


class frmRelacion(HorizontalModelForm):
    """
    Formulario principal de Relación

    Campos
    ------
    - campo_izquierda
    - tipo
    - campo_derecha
    """

    class Meta:
        model = Relacion
        fields = [
            'campo_izquierda'
            'tipo'
            'campo_derecha'
        ]
