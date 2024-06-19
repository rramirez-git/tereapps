from django import forms

from zend_django.hiperforms import HorizontalModelForm

from .models import Estadistico


class frmEstadistico(HorizontalModelForm):

    class Meta:
        model = Estadistico
        fields = [
            'periodo',
            'cantidad',
        ]
        widgets = {
            'periodo': forms.TextInput(attrs={'type': 'date'})
        }
