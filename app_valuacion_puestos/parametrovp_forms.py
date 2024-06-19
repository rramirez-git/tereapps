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
from .parametrovp_models import ParametroVP
from zend_django.hiperforms import HorizontalModelForm


class frmParametroVP(HorizontalModelForm):
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


class frmParametroVP_Read(HorizontalModelForm):
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
