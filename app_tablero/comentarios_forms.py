"""
Formularios para modelo Comentario

Formularios
-----------
frmComentario
"""
from zend_django.hiperforms import HorizontalModelForm

from .models import Comentario

class frmComentario(HorizontalModelForm):
    """Formulario principal del modelo Comentario"""

    class Meta:
        model = Comentario
        fields = [
            'usuario',
            'en_respuesta_a',
            'objeto',
            'objeto_tipo',
            'comentario',
        ]
