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
from django import forms

from .factor_models import Factor


class frmFactor(forms.ModelForm):
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
            'exponente',
        ]


class frmFactorRead(forms.ModelForm):
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
    cantidad_de_niveles = forms.IntegerField(required=False, initial=0)

    class Meta:
        model = Factor
        fields = [
            'factor',
            'posicion',
            'ponderacion_nivel_1',
            'exponente',
        ]

    field_order = [
        'factor',
        'posicion',
        'ponderacion_nivel_1',
        'exponente',
        'cantidad_de_niveles', ]
