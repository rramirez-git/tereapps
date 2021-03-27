"""
Vistas relacionadas con el modelo MenuOpc (Opciones de Menú Principal)

Vistas
------
- List
- Read
- Create
- Update
- Delete
"""
from django.shortcuts import render
from django.views import View

from .menuopc_forms import frmMenuOpc as base_form
from .menuopc_models import MenuOpc as main_model
from .views import GenericCreate
from .views import GenericDelete
from .views import GenericList
from .views import GenericRead
from .views import GenericUpdate


def template_base_path(file):
    return 'zend_django/menuopc/' + file + ".html"


class List(View):
    tereapp = 'administrar'

    def base_render(self, request):
        data = list(main_model.objects.filter(padre=None))
        toolbar = []
        return render(request, template_base_path("list"), {
            'titulo': "Menú Principal",
            'titulo_descripcion': "",
            'toolbar': toolbar,
            'footer': False,
            'read_only': False,
            'alertas': [],
            'req_chart': False,
            'data': data,
            'tereapp': self.tereapp,
        })

    def get(self, request):
        return self.base_render(request)

    def post(self, request):
        return self.base_render(request)


class Read(GenericRead):
    titulo_descripcion = "Menú Principal (opciones)"
    model_name = "menuopc"
    base_data_form = base_form
    main_data_model = main_model
    tereapp = 'administrar'


class Create(GenericCreate):
    titulo = "Menú Principal (opciones)"
    model_name = "menuopc"
    base_data_form = base_form
    tereapp = 'administrar'


class Update(GenericUpdate):
    titulo = "Menú Principal (opciones)"
    model_name = "menuopc"
    base_data_form = base_form
    main_data_model = main_model
    tereapp = 'administrar'


class Delete(GenericDelete):
    model_name = "menuopc"
    main_data_model = main_model
    tereapp = 'administrar'
