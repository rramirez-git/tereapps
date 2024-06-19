"""
Formularios para modelo Factor

Formularios
-----------
frmFactor
    Formulario de Captura y Actualización
    - factor
    - posicion
    - ponderacion_nivel_1
    - exponente

frmFactorRead
    Formulario de Lectura
    - factor
    - posicion
    - ponderacion_nivel_1
    - exponente
    - cantidad_de_niveles
"""
from .factor_models import Factor

from zend_django.hiperforms import HorizontalModelForm


class frmFactor(HorizontalModelForm):
    """
    Formulario principal del modelo Factor

    Campos
    ------
    - factor
    - posicion
    - ponderacion_nivel_1
    - exponente
    """

    class Meta:
        model = Factor
        fields = [
            'factor',
            'posicion',
            'ponderacion_nivel_1',
        ]


class frmFactorRead(HorizontalModelForm):
    """
    Formulario para mostrar el modelo Factor

    Campos
    ------
    - factor
    - posicion
    - ponderacion_nivel_1
    - exponente
    - cantidad_de_niveles
    """

    class Meta:
        model = Factor
        fields = [
            'factor',
            'ponderacion_nivel_1',
        ]

    field_order = [
        'factor',
        'ponderacion_nivel_1', ]
