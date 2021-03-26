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
        model: Favorito
        fields = [
            'usuario',
            'etiqueta',
            'url',
        ]
        widgets = {
            'usuario': forms.HiddenInput()
        }
