"""
Formularios para modelo Favorito (Mis Favoritos)

Formularios
-----------
frmFavs
    Formulario Completo del modelo
    - usuario (hidden)
    - url
    - etiqueta
"""
from django import forms

from .admin_models import Favorito
from zend_django.hiperforms import HorizontalModelForm


class frmFavorito(HorizontalModelForm):
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
            'etiqueta',
            'url',
        ]
