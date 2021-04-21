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
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from zend_django.templatetags.op_helpers import crud_label
from zend_django.templatetags.utils import GenerateReadCRUDToolbar
from zend_django.views import GenericCreate
from zend_django.views import GenericDelete
from zend_django.views import GenericList
from zend_django.views import GenericRead
from zend_django.views import GenericUpdate

from .puesto_forms import frmPuesto as base_form
from .puesto_forms import frmPuestoRead
from .puesto_models import Puesto as main_model
from .models import Factor, Nivel, Ponderacion


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
    html_template = template_base_path('form')
    titulo_descripcion = "Puesto"
    model_name = "puesto"
    base_data_form = frmPuestoRead
    main_data_model = main_model
    tereapp = 'valuacion_de_puestos'

    def get(self, request, pk):
        if not self.main_data_model.objects.filter(pk=pk).exists():
            return HttpResponseRedirect(reverse('item_no_encontrado'))
        obj = self.main_data_model.objects.get(pk=pk)
        form = self.base_data_form(instance=obj)
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
            'factores': list(Factor.objects.all()),
        })


class Create(GenericCreate):
    html_template = template_base_path('form')
    titulo = "Puesto"
    model_name = "puesto"
    base_data_form = base_form
    tereapp = 'valuacion_de_puestos'

    def base_render(self, request, forms):
        return render(request, self.html_template, {
            'titulo': self.titulo,
            'titulo_descripcion': crud_label('create'),
            'toolbar': None,
            'footer': False,
            'read_only': False,
            'alertas': [],
            'req_chart': False,
            'search_value': '',
            'forms': forms,
            'tereapp': self.tereapp,
            'factores': list(Factor.objects.all()),
        })

    def post(self, request):
        form = self.base_data_form(request.POST, files=request.FILES)
        if form.is_valid():
            obj = form.save()
            for factor in Factor.objects.all():
                Ponderacion.objects.create(
                    puesto=obj,
                    nivel=Nivel.objects.get(
                        pk=request.POST.get(f"factor_{factor.pk}"))
                )
            return HttpResponseRedirect(reverse(
                f'{self.model_name}_read',
                kwargs={'pk': obj.pk}))
        return self.base_render(request, {'top': [{'form': form}]})


class Update(GenericUpdate):
    html_template = template_base_path('form')
    titulo = "Puesto"
    model_name = "puesto"
    base_data_form = base_form
    main_data_model = main_model
    tereapp = 'valuacion_de_puestos'

    def base_render(self, request, form, obj):
        return render(request, self.html_template, {
            'titulo': self.titulo,
            'titulo_descripcion': crud_label('update'),
            'toolbar': None,
            'footer': False,
            'read_only': False,
            'alertas': [],
            'req_chart': False,
            'search_value': '',
            'forms': {'top': [{'form': form}]},
            'tereapp': self.tereapp,
            'object': obj,
            'factores': list(Factor.objects.all()),
        })

    def post(self, request, pk):
        if not self.main_data_model.objects.filter(pk=pk).exists():
            return HttpResponseRedirect(reverse('item_no_encontrado'))
        obj = self.main_data_model.objects.get(pk=pk)
        form = self.base_data_form(
            instance=obj, data=request.POST, files=request.FILES)
        if form.is_valid():
            obj = form.save()
            obj.niveles_ponderacion.all().delete()
            for factor in Factor.objects.all():
                Ponderacion.objects.create(
                    puesto=obj,
                    nivel=Nivel.objects.get(
                        pk=request.POST.get(f"factor_{factor.pk}"))
                )
            return HttpResponseRedirect(reverse(
                f'{self.model_name}_read',
                kwargs={'pk': obj.pk}))
        return self.base_render(request, form, obj)


class Delete(GenericDelete):
    model_name = "puesto"
    main_data_model = main_model
