from django.db import IntegrityError
from django.db.models import ProtectedError
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from zend_django.templatetags.op_helpers import crud_label
from zend_django.templatetags.utils import GenerateReadCRUDToolbar
from zend_django.views import GenericCreate
from zend_django.views import GenericDelete
from zend_django.views import GenericRead
from zend_django.views import GenericUpdate, GenericList
from zend_django.models import ParametroUsuario

from .models import Cuenta, EstadisticoAnual as main_model
from .estad_anual_forms import frmEstadisticoAnual as base_form

def template_base_path(file):
    return 'app_tablero/estadistico_anual/' + file + ".html"


class List(GenericList):
    html_template = template_base_path("list")
    titulo = "Estadisticos Anuales"
    titulo_descripcion = ""
    main_data_model = main_model
    model_name = "estadisticoanual"
    tereapp = 'tableros'

    def get_data(self, pk_cta,search_value=''):
        return self.main_data_model.objects.filter(cuenta_id=pk_cta)

    def base_render(self, request, data, search_value, pk_cta):
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
            'pk_cta': pk_cta,
            'tereapp': self.tereapp,
        })

    def get(self, request, pk):
        search_value = ParametroUsuario.get_valor(
            request.user, 'basic_search', self.model_name)
        return self.base_render(
            request, self.get_data(pk, search_value), search_value, pk)

    def post(self, request, pk):
        if "search" == request.POST.get('action', ''):
            search_value = request.POST.get('valor', '')
        else:
            search_value = ParametroUsuario.get_valor(
                request.user, 'basic_search', self.model_name)
        return self.base_render(
            request, self.get_data(pk, search_value), search_value, pk)


class Read(GenericRead):
    # html_template = template_base_path('see')
    titulo_descripcion = "Estadistico Anual"
    model_name = "estadisticoanual"
    base_data_form = base_form
    main_data_model = main_model
    tereapp = 'tableros'

    def get(self, request, pk):
        if not self.main_data_model.objects.filter(pk=pk).exists():
            return HttpResponseRedirect(reverse('item_no_encontrado'))
        obj = self.main_data_model.objects.get(pk=pk)
        form = self.base_data_form(instance=obj)
        toolbar = GenerateReadCRUDToolbar(
            request, self.model_name, obj, self.main_data_model)
        toolbar[0].update({'type': 'link_pk', 'pk': obj.cuenta.pk})
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
    titulo = "Estadistico Anual"
    model_name = "estadisticoanual"
    base_data_form = base_form
    tereapp = 'tableros'

    def get(self, request, pk_padre):
        return self.base_render(request, {
            'top': [{'form': self.base_data_form()}]})

    def post(self, request, pk_padre):
        form = self.base_data_form(request.POST, files=request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.cuenta = Cuenta.objects.get(pk=pk_padre)
            obj.save()
            return HttpResponseRedirect(reverse(
                f'{self.model_name}_read',
                kwargs={'pk': obj.pk}))
        return self.base_render(request, {'top': [{'form': form}]})


class Update(GenericUpdate):
    titulo = "Estadistico Anual"
    model_name = "estadisticoanual"
    base_data_form = base_form
    main_data_model = main_model
    tereapp = 'tableros'

    def post(self, request, pk):
        if not self.main_data_model.objects.filter(pk=pk).exists():
            return HttpResponseRedirect(reverse('item_no_encontrado'))
        obj = self.main_data_model.objects.get(pk=pk)
        form = self.base_data_form(
            instance=obj, data=request.POST, files=request.FILES)
        if form.is_valid():
            obj = form.save()
            return HttpResponseRedirect(reverse(
                f'{self.model_name}_read',
                kwargs={'pk': obj.pk}))
        return self.base_render(request, form, obj)


class Delete(GenericDelete):
    model_name = "cuenta"
    main_data_model = main_model

    def get(self, request, pk):
        if not self.main_data_model.objects.filter(pk=pk).exists():
            return HttpResponseRedirect(reverse('item_no_encontrado'))
        obj = self.main_data_model.objects.get(pk=pk)
        try:
            pk_cuenta = obj.cuenta.pk
            obj.delete()
            return HttpResponseRedirect(reverse(
                f'{self.model_name}_list', kwargs={'pk': pk_cuenta}))
        except ProtectedError:
            return HttpResponseRedirect(reverse('item_con_relaciones'))
        except IntegrityError:
            return HttpResponseRedirect(reverse('item_con_relaciones'))
