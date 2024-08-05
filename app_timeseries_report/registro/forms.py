from zend_django.hiperforms import HorizontalModelForm, HorizontalForm
from django import forms


class frmUploadUpdateFile(HorizontalForm):
    archivo = forms.FileField(required=True)
