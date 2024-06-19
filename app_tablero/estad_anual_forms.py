from zend_django.hiperforms import HorizontalModelForm

from .models import EstadisticoAnual


class frmEstadisticoAnual(HorizontalModelForm):

    class Meta:
        model = EstadisticoAnual
        fields = [
            'anio',
            'cantidad'
        ]
