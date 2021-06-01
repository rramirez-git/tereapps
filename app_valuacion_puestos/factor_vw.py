"""
Vistas relacionadas con el modelo Factor

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

from .factor_forms import frmFactor as base_form
from .factor_forms import frmFactorRead
from .factor_models import Factor as main_model


def template_base_path(file):
    return 'app_valuacion_puestos/factor/' + file + ".html"


class List(GenericList):
    html_template = template_base_path("list")
    titulo = "Factor"
    titulo_descripcion = ""
    main_data_model = main_model
    model_name = "factor"
    tereapp = 'valuacion_de_puestos'

    def get_data(self, search_value=''):
        if '' == search_value:
            return list(
                self.main_data_model.objects.all())
        else:
            return list(self.main_data_model.objects.filter(
                Q(factor__icontains=search_value)))

    def base_render(self, request, data, search_value):
        ParametroUsuario.set_valor(
                request.user, 'basic_search', self.model_name, search_value)
        suma = 0
        for reg in data:
            suma += reg.ponderacion_nivel_1
        alertas = []
        if suma < 99 or suma > 101:
            alertas.append("La suma de ponderaciones No es 100%")
        return render(request, self.html_template, {
            'titulo': self.titulo,
            'titulo_descripcion': self.titulo_descripcion,
            'toolbar': [{'type': 'search'}],
            'footer': False,
            'read_only': False,
            'alertas': alertas,
            'req_chart': False,
            'search_value': search_value,
            'data': data,
            'tereapp': self.tereapp,
            'suma': suma
        })


class Read(GenericRead):
    html_template = template_base_path('see')
    titulo_descripcion = "Factor"
    model_name = "factor"
    base_data_form = frmFactorRead
    main_data_model = main_model
    tereapp = 'valuacion_de_puestos'

    def get(self, request, pk):
        if not self.main_data_model.objects.filter(pk=pk).exists():
            return HttpResponseRedirect(reverse('item_no_encontrado'))
        obj = self.main_data_model.objects.get(pk=pk)
        form = self.base_data_form(
            instance=obj,
            initial={
                'cantidad_de_niveles': obj.cantidad_de_niveles,
                'exponente': obj.exponente,
            })
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
            'withoutBtnSave': True,
        })


class Create(GenericCreate):
    titulo = "Factor"
    model_name = "factor"
    base_data_form = base_form
    tereapp = 'valuacion_de_puestos'


class Update(GenericUpdate):
    titulo = "Factor"
    model_name = "factor"
    base_data_form = base_form
    main_data_model = main_model
    tereapp = 'valuacion_de_puestos'


class Delete(GenericDelete):
    model_name = "factor"
    main_data_model = main_model
