from zend_django.hiperforms import HorizontalModelForm, HorizontalForm
from django import forms

from .models import ReporteTS

class frmMain(HorizontalModelForm):

    class Meta:
        model = ReporteTS
        fields = [
            'nombre',
            'concepto_predefinido',
        ]
