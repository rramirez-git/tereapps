from typing import Any
from django.shortcuts import render

from django.views import View

from . import dpt_test01, dpt_test02, dpt_test03, dpt_test04, dpt_test05


def template_base_path(file):
    return 'dash_plotly_testing/' + file + ".html"


class ViewDPTGeneric(View):
    html_template = template_base_path('index')
    titulo = "Test 01"
    titulo_descripcion = "Dash Plotly Test"
    tereapp = 'administrar'
    dp_name=  "DPTTest"

    def setValues(self, idxno):
        self.html_template = template_base_path('test')
        self.titulo = f"Test {idxno:02}"
        self.dp_name += f'{idxno:02}'

    def get(self, request):
        return render(request, self.html_template, {
            'titulo': self.titulo,
            'titulo_descripcion': self.titulo_descripcion,
            'tereapp': self.tereapp,
            'dp_name': self.dp_name,
        })


class ViewIndex(ViewDPTGeneric):

    def get(self, request):
        return super().get(request)


class ViewTest1(ViewDPTGeneric):

    def get(self, request):
        self.setValues(1)
        return super().get(request)

class ViewTest2(ViewDPTGeneric):

    def get(self, request):
        self.setValues(2)
        return super().get(request)

class ViewTest3(ViewDPTGeneric):

    def get(self, request):
        self.setValues(3)
        return super().get(request)

class ViewTest4(ViewDPTGeneric):

    def get(self, request):
        self.setValues(4)
        return super().get(request)

class ViewTest5(ViewDPTGeneric):

    def get(self, request):
        self.setValues(5)
        return super().get(request)
