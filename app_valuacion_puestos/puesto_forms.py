"""
Formularios pata modelo Puesto

Formularios
-----------
frmPuesto
    Formulario de Captura y Actualización
    - puesto
    - posicion
    - estatus

frmPuestoRead
    Formulario de Lectura
    - puesto
    - posicion
    - estatus
    - ponderacion_total
"""
from django import forms

from .puesto_models import Puesto


class frmPuesto(forms.ModelForm):
    """
    Formulario principal del modelo Puesto

    Campos
    ------
    - puesto
    - posicion
    - estatus
    """

    class Meta:
        model = Puesto
        fields = [
            'puesto',
            'posicion',
            'estatus',
        ]
        widgets = {
            'estatus': forms.CheckboxInput(attrs={
                'class': 'action-on-reg',
                'data-toggle': "toggle",
                'data-size': "xs",
                'data-onstyle': "secondary",
                'data-style': "ios",
                'data-on': " ",
                'data-off': " ", })
        }

    field_order = ['puesto', 'estatus', 'posicion']


class frmPuestoRead(forms.ModelForm):
    """
    Formulario para mostrar el modelo Puesto

    Campos
    ------
    - puesto
    - posicion
    - estatus
    - ponderacion_total
    """
    ponderacion_total = forms.DecimalField(
        max_digits=6, decimal_places=2, required=False, initial=0.0)

    class Meta:
        model = Puesto
        fields = [
            'puesto',
            'posicion',
            'estatus',
        ]
        widgets = {
            'estatus': forms.CheckboxInput(attrs={
                'class': 'action-on-reg',
                'data-toggle': "toggle",
                'data-size': "xs",
                'data-onstyle': "secondary",
                'data-style': "ios",
                'data-on': " ",
                'data-off': " ", })
        }

    field_order = ['puesto', 'estatus', 'posicion', 'ponderacion_total']
