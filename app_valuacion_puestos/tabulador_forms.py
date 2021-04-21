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
    - cantidad_de_niveles
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
    - cantidad_de_niveles
    """
    cantidad_de_niveles = forms.IntegerField(required=False, initial=0)

    class Meta:
        model = Tabulador
        fields = [
            'tabulador',
        ]

    field_order = [
        'tabulador',
        'cantidad_de_niveles',
    ]
