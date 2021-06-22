"""
Formularios para modelo Cuenta

Formularios
-----------
frmComentario
"""
from zend_django.hiperforms import HorizontalModelForm

from .models import Cuenta


class frmCuenta(HorizontalModelForm):
    """Formulario principal del modelo Comentario"""

    class Meta:
        model = Cuenta
        fields = [
            'tablero',
            'pre_cve',
            'pre_posicion',
            'pre_cve_2',
            'nivel',
            'entidad',
            'cuenta',
            'descripcion',
            'formato',
        ]
