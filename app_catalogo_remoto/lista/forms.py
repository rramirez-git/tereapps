from zend_django.hiperforms import HorizontalModelForm

from .models import ListaCatalogo


class frmMain(HorizontalModelForm):

    class Meta:
        model = ListaCatalogo
        fields = [
            'nombre',
            'usr',
        ]
