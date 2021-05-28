"""
Formularios para modelo Tabulador

Formularios
-----------
frmTabulador
    Formulario de Captura y Actualización
    - tabulador

frmTabuladorRead
    Formulario de Lectura
    - tabulador
"""
from django import forms

from .tabulador_models import Tabulador


class frmTabulador(forms.ModelForm):
    """
    Formulario principal del modelo Tabulador

    Campos
    ------
    - tabulador
    """

    class Meta:
        model = Tabulador
        fields = [
            'tabulador',
        ]


class frmTabuladorRead(forms.ModelForm):
    """
    Formulario para mostrar el modelo Tabulador

    Campos
    ------
    - tabulador
    """

    class Meta:
        model = Tabulador
        fields = [
            'tabulador',
        ]

    field_order = [
        'tabulador',
    ]
