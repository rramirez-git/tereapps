"""
Formularios para modelo Nivel

Formularios
-----------
frmNivel
    Formulario de Captura y Actualización
    - nivel_multiplicador
    - nivel

frmNivelRead
    Formulario de Lectura
    - nivel_multiplicador
    - nivel
    - ponderacion
"""
from django import forms

from .nivel_models import Nivel

class frmNivel(forms.ModelForm):
    """
    Formulario principal del modelo Nivel

    Campos
    ------
    - nivel_multiplicador
    - nivel
    """

    class Meta:
        model = Nivel
        fields = [
            'nivel_multiplicador',
            'nivel',
        ]


class frmNivelRead(forms.ModelForm):
    """
    Formulario para mostrar el modelo Nivel

    Campos
    ------
    - nivel_multiplicador
    - nivel
    - ponderacion
    """
    ponderacion = forms.DecimalField(max_digits=6, decimal_places=2, required=False)

    class Meta:
        model = Nivel
        fields = [
            'nivel_multiplicador',
            'nivel',
        ]

    field_order = [
        'nivel_multiplicador',
        'nivel',
        'ponderacion',
    ]
