"""
Vistas relacionadas con el modelo Tabulador

Vistas
------
- List
- Read
- Create
- Update
- Delete
"""
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from zend_django.parametros_models import ParametroUsuario
from zend_django.templatetags.utils import GenerateReadCRUDToolbar
from zend_django.views import GenericCreate
from zend_django.views import GenericDelete
from zend_django.views import GenericList
from zend_django.views import GenericRead
from zend_django.views import GenericUpdate

from .tabulador_forms import frmTabulador as base_form
from .tabulador_forms import frmTabuladorRead
from .tabulador_models import Tabulador as main_model


def template_base_path(file):
    return 'app_valuacion_puestos/tabulador/' + file + ".html"


class List(GenericList):
    html_template = template_base_path("list")
    titulo = "Tabuladores"
    titulo_descripcion = ""
    main_data_model = main_model
    model_name = "tabulador"
    tereapp = 'valuacion_de_puestos'

    def get_data(self, search_value=''):
        if '' == search_value:
            return list(
                self.main_data_model.objects.all())
        else:
            return list(self.main_data_model.objects.filter(
                Q(factor__icontains=search_value)))


class Read(GenericRead):
    html_template = template_base_path('see')
    titulo_descripcion = "Tabulador"
    model_name = "tabulador"
    base_data_form = frmTabuladorRead
    main_data_model = main_model
    tereapp = 'valuacion_de_puestos'

    def get(self, request, pk):
        if not self.main_data_model.objects.filter(pk=pk).exists():
            return HttpResponseRedirect(reverse('item_no_encontrado'))
        obj = self.main_data_model.objects.get(pk=pk)
        form = self.base_data_form(
            instance=obj,
            initial={'cantidad_de_niveles': obj.cantidad_de_niveles,})
        toolbar = GenerateReadCRUDToolbar(
            request, self.model_name, obj, self.main_data_model)
        return render(request, self.html_template, {
            'titulo': obj,
            'titulo_descripcion': self.titulo_descripcion,
            'toolbar': toolbar,
            'footer': False,
            'read_only': True,
            'alertas': [],
            'req_chart': False,
            'search_value': '',
            'forms': {'top': [{'form': form}]},
            'tereapp': self.tereapp,
            'object': obj,
        })


class Create(GenericCreate):
    titulo = "Tabulador"
    model_name = "tabulador"
    base_data_form = base_form
    tereapp = 'valuacion_de_puestos'


class Update(GenericUpdate):
    titulo = "Tabulador"
    model_name = "tabulador"
    base_data_form = base_form
    main_data_model = main_model
    tereapp = 'valuacion_de_puestos'


class Delete(GenericDelete):
    model_name = "tabulador"
    main_data_model = main_model
