"""
Formularios para modelo CampoReporte

Formularios
-----------

frmCampoReporte
    Formulario Completo
    - campo
    - posicion
    - tipo
    - valor_default
    - mostrar
"""
from django import forms

from .reporte_models import CampoReporte
from zend_django.hiperforms import HorizontalModelForm


class frmCampoReporte(HorizontalModelForm):
    """
    Formulario para el modelo CampoReporte

    Campos
    ------
    - campo
    - posicion
    - tipo
    - valor_default
    - mostrar
    - es_llave
    """

    class Meta:
        model = CampoReporte
        fields = [
            'campo',
            'posicion',
            'tipo',
            'valor_default',
            'mostrar',
            'es_llave',
        ]
