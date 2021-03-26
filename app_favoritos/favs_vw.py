"""
Vistas relacionadas con el modelo Favorito, propios del usuario en sesion

Vistas
------
- List
- Read
- Create
- Update
- Delete
- Set
- Get
"""
from django.db.models import Q
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse

from zend_django.views import GenericCreate
from zend_django.views import GenericDelete
from zend_django.views import GenericList
from zend_django.views import GenericRead
from zend_django.views import GenericUpdate
from zend_django.views import View

from .admin_models import Favorito as main_model
from .favs_forms import frmFavorito as base_form

def template_base_path(file):
    return 'app_favoritos/favs/' + file + ".html"

class List(GenericList):
    html_template = template_base_path("list")
    titulo = "Favoritos"
    titulo_descripcion = ""
    main_data_model = main_model
    model_name = "favorito"
    tereapp = 'administrar'

    def get_data(self, search_value=''):
        if '' == search_value:
            return list(
                self.main_data_model.objects.all())
        else:
            return list(self.main_data_model.objects.filter(
                Q(usuario__first_name__icontains=search_value) |
                Q(usuario__last_name__icontains=search_value) |
                Q(usuario__profile__apellido_materno__icontains=search_value) |
                Q(etiqueta__icontains=search_value) |
                Q(url__icontains=search_value)))


class Read(GenericRead):
    titulo_descripcion = "Favorito"
    model_name = "favorito"
    base_data_form = base_form
    main_data_model = main_model
    tereapp = 'mis_favoritos'


class Create(GenericCreate):
    titulo = "Favorito"
    model_name = "favorito"
    base_data_form = base_form
    tereapp = 'mis_favoritos'


class Update(GenericUpdate):
    titulo = "Favorito"
    model_name = "favorito"
    base_data_form = base_form
    main_data_model = main_model
    tereapp = 'mis_favoritos'


class Delete(GenericDelete):
    model_name = "favorito"
    main_data_model = main_model

class Get(View):

    def base_render(self, request):
        #data = list(main_model.objects.filter(
        #    usuario=request.user).values('pk','etiqueta', 'url'))
        #return JsonResponse(data, safe=False)
        return render(request,template_base_path('get'), {})

    def get(self, request):
        return self.base_render(request)

    def post(self, request):
        return self.base_render(request)

class Set(View):
    pass
