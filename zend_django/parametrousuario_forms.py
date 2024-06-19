"""
Formularios para modelo ParametroUsuario

Formularios
-----------
frmParametroUsuario
    Formulario Completo
    - seccion
    - nombre
    - valor_default
    - tipo
"""
from .hiperforms import HorizontalModelForm
from .parametros_models import ParametroUsuario


class frmParametroUsuario(HorizontalModelForm):
    """
    Formulario principal del modelo ParametroUsuario

    Campos
    ------
    - seccion
    - nombre
    - valor_default
    - tipo
    """

    class Meta:
        model = ParametroUsuario
        fields = [
            'seccion',
            'nombre',
            'valor_default',
            'tipo',
        ]
