from django.db.models import Q
from django.shortcuts import render

from zend_django.parametros_models import ParametroUsuario
from zend_django.views import GenericCreate
from zend_django.views import GenericDelete
from zend_django.views import GenericList
from zend_django.views import GenericRead
from zend_django.views import GenericUpdate

from .tablero_models import Tablero as main_model
from .tablero_forms import frmTablero as base_form


def template_base_path(file):
    return 'app_tablero/tablero/' + file + ".html"


class List(GenericList):
    html_template = template_base_path("list")
    titulo = "Tablero"
    titulo_descripcion = ""
    main_data_model = main_model
    model_name = "tablero"
    tereapp = 'tableros'

    def get_data(self, search_value=''):
        if '' == search_value:
            return list(
                self.main_data_model.objects.all())
        else:
            return list(self.main_data_model.objects.filter(
                Q(nombre__icontains=search_value)
                | Q(nombre_de_archivo__icontains=search_value)))

    def base_render(self, request, data, search_value):
        data = [{
            'pk': reg.pk,
            'nombre': reg.nombre,
            'nombre_de_archivo': reg.nombre_de_archivo,
            'displayable2user': reg.displayable2user(request.user),
            } for reg in data]
        ParametroUsuario.set_valor(
            request.user, 'basic_search', self.model_name, search_value)
        return render(request, self.html_template, {
            'titulo': self.titulo,
            'titulo_descripcion': self.titulo_descripcion,
            'toolbar': [{'type': 'search'}],
            'footer': False,
            'read_only': False,
            'alertas': [],
            'req_chart': False,
            'search_value': search_value,
            'data': data,
            'tereapp': self.tereapp,
        })


class Read(GenericRead):
    html_template = template_base_path('see')
    titulo_descripcion = "Tablero"
    model_name = "tablero"
    base_data_form = base_form
    main_data_model = main_model
    tereapp = 'tableros'


class Create(GenericCreate):
    titulo = "Tablero"
    model_name = "tablero"
    base_data_form = base_form
    tereapp = 'tableros'


class Update(GenericUpdate):
    titulo = "Tablero"
    model_name = "tablero"
    base_data_form = base_form
    main_data_model = main_model
    tereapp = 'tableros'


class Delete(GenericDelete):
    model_name = "tablero"
    main_data_model = main_model
