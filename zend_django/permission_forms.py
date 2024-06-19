"""
Formularios para modelo Permission

Formularios
-----------
frmPermission
    Formulario Completo
    - name
    - content_type
    - codename
"""
from .hiperforms import HorizontalModelForm
from django.contrib.auth.models import Permission


class frmPermission(HorizontalModelForm):
    """
    Formulario principal del modelo Permission

    Campos
    ------
    - name
    - content_type
    - codename
    """

    class Meta:
        model = Permission
        fields = [
            'name',
            'content_type',
            'codename',
        ]
        labels = {
            'name': 'Permiso',
            'content_type': 'Tipo',
            'codename': 'Código',
        }
