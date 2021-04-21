"""
Formularios para el modelo ParametroVP

Formularios
-----------
frmParametroVP
    Formulario principal
    - parametro
    - valor

frmParametroVP_Read
    Formulario para Lectura
    - parametro
    - valor
    - fecha
"""
from django import forms

from .parametrovp_models import ParametroVP


class frmParametroVP(forms.ModelForm):
    """
    Formulario principal del modelo ParametroVP

    Campos
    ------
    - parametro
    - valor
    """

    class Meta:
        model = ParametroVP
        fields = [
            'parametro',
            'valor',
        ]

class frmParametroVP_Read(forms.ModelForm):
    """
    Formulario principal del modelo ParametroVP

    Campos
    ------
    - parametro
    - valor
    """

    class Meta:
        model = ParametroVP
        fields = [
            'parametro',
            'valor',
            'fecha'
        ]
