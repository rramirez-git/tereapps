"""
Vistas relacionadas con el modelo Nivel

Vistas
------
- Read
- Create
- Update
- Delete
"""
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.db import IntegrityError
from django.db.models import ProtectedError

from zend_django.views import GenericCreate
from zend_django.views import GenericDelete
from zend_django.views import GenericRead
from zend_django.views import GenericUpdate
from zend_django.templatetags.utils import GenerateReadCRUDToolbar
from zend_django.templatetags.op_helpers import crud_label

from .nivel_forms import frmNivel as base_form, frmNivelRead
from .nivel_models import Nivel as main_model
from .models import Factor


def template_base_path(file):
    return 'app_valuacion_puestos/nivel/' + file + ".html"

class Read(GenericRead):
    #html_template = template_base_path('see')
    titulo_descripcion = "Nivel"
    model_name = "nivel"
    base_data_form = frmNivelRead
    main_data_model = main_model
    tereapp = 'valuacion_de_puestos'

    def get(self, request, pk):
        if not self.main_data_model.objects.filter(pk=pk).exists():
            return HttpResponseRedirect(reverse('item_no_encontrado'))
        obj = self.main_data_model.objects.get(pk=pk)
        form = self.base_data_form(
            instance=obj, initial={'ponderacion': obj.ponderacion})
        toolbar = GenerateReadCRUDToolbar(
            request, self.model_name, obj, self.main_data_model)
        toolbar[0].update({'type': 'link_pk', 'pk': obj.factor.pk})
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
    titulo = "Nivel"
    model_name = "nivel"
    base_data_form = base_form
    tereapp = 'valuacion_de_puestos'

    def base_render(self, request, forms, alertas=[]):
        return render(request, self.html_template, {
            'titulo': self.titulo,
            'titulo_descripcion': crud_label('create'),
            'toolbar': None,
            'footer': False,
            'read_only': False,
            'alertas': alertas,
            'req_chart': False,
            'search_value': '',
            'forms': forms,
            'tereapp': self.tereapp,
        })

    def get(self, request, pk_padre):
        return self.base_render(request, {
            'top': [{'form': self.base_data_form()}]})

    def post(self, request, pk_padre):
        form = self.base_data_form(request.POST, files=request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.factor = Factor.objects.get(pk=pk_padre)
            try:
                obj.save()
            except IntegrityError:
                return self.base_render(
                    request,
                    {'top': [{'form': form}]},
                    ["No es posible agregar el mismo nombre de nivel para un mismo factor"])
            return HttpResponseRedirect(reverse(
                f'{self.model_name}_read',
                kwargs={'pk': obj.pk}))
        return self.base_render(request, {'top': [{'form': form}]})


class Update(GenericUpdate):
    titulo = "Nivel"
    model_name = "nivel"
    base_data_form = base_form
    main_data_model = main_model
    tereapp = 'valuacion_de_puestos'


class Delete(GenericDelete):
    model_name = "nivel"
    main_data_model = main_model

    def get(self, request, pk):
        if not self.main_data_model.objects.filter(pk=pk).exists():
            return HttpResponseRedirect(reverse('item_no_encontrado'))
        obj = self.main_data_model.objects.get(pk=pk)
        try:
            pk_factor = obj.factor.pk
            obj.delete()
            return HttpResponseRedirect(reverse(
                f'{self.model_name}_list', kwargs={'pk': pk_factor}))
        except ProtectedError:
            return HttpResponseRedirect(reverse('item_con_relaciones'))
        except IntegrityError:
            return HttpResponseRedirect(reverse('item_con_relaciones'))
