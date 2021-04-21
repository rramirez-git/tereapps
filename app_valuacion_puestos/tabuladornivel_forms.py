"""
Formularios para modelo TabuladorNivel

Formularios
-----------
frmTabuladorNivel
    Formulario de Captura y Actualización
    - posicion
    - porcentaje
"""
from django import forms

from .tabuladornivel_models import TabuladorNivel


class frmTabuladorNivel(forms.ModelForm):
    """
    Formulario principal del modelo TabuladorNivel

    Campos
    ------
    - nivel_multiplicador
    - nivel
    """

    class Meta:
        model = TabuladorNivel
        fields = [
            'posicion',
            'porcentaje',
        ]
