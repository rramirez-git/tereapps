"""
Vistas relacionadas con el modedlo ParametroVP

Vistas
------
- List
- Read
- Create
- Update
- Delete
"""
from django.db.models import Q

from zend_django.views import GenericCreate
from zend_django.views import GenericDelete
from zend_django.views import GenericList
from zend_django.views import GenericRead
from zend_django.views import GenericUpdate

from .parametrovp_forms import frmParametroVP as base_form, frmParametroVP_Read
from .parametrovp_models import ParametroVP as main_model


def template_base_path(file):
    return 'app_valuacion_puestos/parametrovp/' + file + ".html"


class List(GenericList):
    html_template = template_base_path("list")
    titulo = "Parámetros"
    titulo_descripcion = ""
    main_data_model = main_model
    model_name = "parametrovp"
    tereapp = 'valuacion_de_puestos'

    def get_data(self, search_value=''):
        if '' == search_value:
            return list(
                self.main_data_model.objects.all())
        else:
            return list(self.main_data_model.objects.filter(
                Q(parametro__icontains=search_value)))


class Read(GenericRead):
    html_template = template_base_path('see')
    titulo_descripcion = "Parámetro"
    model_name = "parametrovp"
    base_data_form = frmParametroVP_Read
    main_data_model = main_model
    tereapp = 'valuacion_de_puestos'


class Create(GenericCreate):
    titulo = "Parámetro"
    model_name = "parametrovp"
    base_data_form = base_form
    tereapp = 'valuacion_de_puestos'


class Update(GenericUpdate):
    titulo = "Parámetro"
    model_name = "parametrovp"
    base_data_form = base_form
    main_data_model = main_model
    tereapp = 'valuacion_de_puestos'


class Delete(GenericDelete):
    model_name = "parametrovp"
    main_data_model = main_model


