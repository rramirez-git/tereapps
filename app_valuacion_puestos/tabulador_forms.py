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
from .tabulador_models import Tabulador
from zend_django.hiperforms import HorizontalModelForm


class frmTabulador(HorizontalModelForm):
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


class frmTabuladorRead(HorizontalModelForm):
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
