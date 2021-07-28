from django.shortcuts import render
from django.urls import reverse
from django.views import View
from os import path

from zend_django.views import GenericTereAppRootView

class TablerosView(GenericTereAppRootView):
    html_template = "zend_django/idx_empty.html"
    titulo = "Tableros Contables"
    tereapp = 'tableros'

class TablerosAutoLoadView(View):
    html_template = "zend_django/idx_empty.html"
    titulo = "Tableros Contables - Carga Automática"
    tereapp = 'tableros'
    titulo_descripcion = ''
    toolbar = None

    def get(self, request):
        return render(request, self.html_template, {
            'titulo': self.titulo,
            'titulo_descripcion': self.titulo_descripcion,
            'toolbar': self.toolbar,
            'footer': False,
            'read_only': False,
            'alertas': [],
            'req_chart': False,
            'tereapp': self.tereapp,
        })

class VerTablero(View):
    pass
