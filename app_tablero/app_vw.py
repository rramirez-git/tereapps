from django.shortcuts import render
from django.urls import reverse
from django.views import View
from time import sleep

import threading

from .models import Tablero
from .tablero_proc import TableroProc

from zend_django.views import GenericTereAppRootView

class TablerosView(GenericTereAppRootView):
    html_template = "zend_django/idx_empty.html"
    titulo = "Tableros Contables"
    tereapp = 'tableros'

class TablerosAutoLoadView(View):
    html_template = "app_tablero/tablero/autoload.html"
    titulo = "Tableros Contables"
    tereapp = 'tableros'
    titulo_descripcion = 'Carga Automática'
    toolbar = None

    def get_data(self):
        data = []
        threads = []
        for tablero in Tablero.objects.all():
            tbl = TableroProc(tablero)
            existe = tbl.checkInFTP()
            data.append({
                'tbl': tablero,
                'pk': tablero.pk,
                'nombre': tablero.nombre,
                'existe': existe,
            })
            pso = threading.Thread(target=psa_tablero_thr, args=(tbl,))
            threads.append(pso)
            pso.start()
        wait = True
        while wait:
            sleep(10)
            wait = False
            for pso in threads:
                wait = wait or pso.is_alive()
        return data

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
            'data': self.get_data(),
        })


def psa_tablero_thr(tablero):
    print(f"Iniciando para {tablero.tabl}")
    tablero.process()
    print(f"Terminando para {tablero.tabl}")

class VerTablero(View):
    html_template = "app_tablero/tablero/view.html"
    titulo = ""
    tereapp = 'tableros'
    titulo_descripcion = 'Tablero Contable'
    toolbar = None

    def get(self, request, pk):
        tbl = Tablero.objects.get(pk=pk)
        print(f'{tbl.anios}')
        return render(request, self.html_template, {
            'titulo': tbl,
            'titulo_descripcion': self.titulo_descripcion,
            'toolbar': self.toolbar,
            'footer': False,
            'read_only': False,
            'alertas': [],
            'req_chart': False,
            'tereapp': self.tereapp,
            'object': tbl,
        })


