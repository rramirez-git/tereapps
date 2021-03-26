"""
Formularios para modelo Favorito

Formularios
-----------
frmFavorito
    Formulario Completo
    - usuario
    - url
    - etiqueta
"""
from django import forms

from .admin_models import Favorito

class frmFavorito(forms.ModelForm):
    """
    Formulario principal del modelo Favorito

    Campos
    ------
    - usuario
    - url
    - etiqueta
    """

    class Meta:
        model = Favorito
        fields = [
            'usuario',
            'etiqueta',
            'url',
        ]
