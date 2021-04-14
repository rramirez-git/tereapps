"""
Vistas relacionadas con el modelo Puesto

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

from .puesto_forms import frmPuesto as base_form
from .puesto_forms import frmPuestoRead
from .puesto_models import Puesto as main_model


def template_base_path(file):
    return 'app_valuacion_puestos/puesto/' + file + ".html"


class List(GenericList):
    html_template = template_base_path("list")
    titulo = "Puesto"
    titulo_descripcion = ""
    main_data_model = main_model
    model_name = "puesto"
    tereapp = 'valuacion_de_puestos'

    def get_data(self, search_value=''):
        if '' == search_value:
            return list(
                self.main_data_model.objects.all())
        else:
            return list(self.main_data_model.objects.filter(
                Q(puesto__icontains=search_value)))


class Read(GenericRead):
    # html_template = template_base_path('see')
    titulo_descripcion = "Puesto"
    model_name = "puesto"
    base_data_form = frmPuestoRead
    main_data_model = main_model
    tereapp = 'valuacion_de_puestos'


class Create(GenericCreate):
    titulo = "Puesto"
    model_name = "puesto"
    base_data_form = base_form
    tereapp = 'valuacion_de_puestos'


class Update(GenericUpdate):
    titulo = "Puesto"
    model_name = "puesto"
    base_data_form = base_form
    main_data_model = main_model
    tereapp = 'valuacion_de_puestos'


class Delete(GenericDelete):
    model_name = "puesto"
    main_data_model = main_model
