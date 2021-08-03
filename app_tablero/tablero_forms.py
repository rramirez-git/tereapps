from zend_django.hiperforms import HorizontalModelForm

from .tablero_models import Tablero

class frmTablero(HorizontalModelForm):

    class Meta:
        model = Tablero

        fields = [
            'nombre',
            'nombre_de_archivo',
            'cuentas_base',
        ]
