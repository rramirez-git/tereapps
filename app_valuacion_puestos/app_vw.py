import json

from django.db.models import Q
from django.shortcuts import render

from zend_django.views import GenericTereAppRootView
from zend_django.views import GenericList
from .puesto_models import Puesto as main_model
from zend_django.parametros_models import ParametroUsuario
from .models import Factor


def template_base_path(file):
    return 'app_valuacion_puestos/reportes/' + file + ".html"


class ValuacionPuestosView(GenericTereAppRootView):
    html_template = "zend_django/idx_empty.html"
    titulo = "Valuación de Puestos"
    tereapp = 'valuacion_de_puestos'


class ReporteFactPPuestoPtos(GenericList):
    html_template = template_base_path("fp_ptos")
    titulo = "Factor por Puesto - Puntos"
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

    def base_render(self, request, data, search_value):
        ParametroUsuario.set_valor(
                request.user, 'basic_search', 'vp_rep_f_psto_ptos', search_value)
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
            'factores': list(Factor.objects.all()),
            'tereapp': self.tereapp,
        })

    def get(self, request):
        search_value = ParametroUsuario.get_valor(
            request.user, 'basic_search', 'vp_rep_f_psto_ptos')
        return self.base_render(
            request, self.get_data(search_value), search_value)

    def post(self, request):
        if "search" == request.POST.get('action', ''):
            search_value = request.POST.get('valor', '')
        else:
            search_value = ParametroUsuario.get_valor(
                request.user, 'basic_search', 'vp_rep_f_psto_ptos')
        return self.base_render(
            request, self.get_data(search_value), search_value)


class ReporteFactPPuestoNiveles(GenericList):
    html_template = template_base_path("fp_niveles")
    titulo = "Factor por Puesto - Niveles"
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

    def base_render(self, request, data, search_value):
        ParametroUsuario.set_valor(
                request.user, 'basic_search', 'vp_rep_f_psto_nvl', search_value)
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
            'factores': list(Factor.objects.all()),
            'tereapp': self.tereapp,
        })

    def get(self, request):
        search_value = ParametroUsuario.get_valor(
            request.user, 'basic_search', 'vp_rep_f_psto_nvl')
        return self.base_render(
            request, self.get_data(search_value), search_value)

    def post(self, request):
        if "search" == request.POST.get('action', ''):
            search_value = request.POST.get('valor', '')
        else:
            search_value = ParametroUsuario.get_valor(
                request.user, 'basic_search', 'vp_rep_f_psto_nvl')
        return self.base_render(
            request, self.get_data(search_value), search_value)


class ReporteValorPPuesto(GenericList):
    html_template = template_base_path("vp")
    titulo = "Valor por Puesto"
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

    def base_render(self, request, data, search_value):
        ParametroUsuario.set_valor(
                request.user, 'basic_search', 'vp_rep_v_psto', search_value)
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

    def get(self, request):
        search_value = ParametroUsuario.get_valor(
            request.user, 'basic_search', 'vp_rep_v_psto')
        return self.base_render(
            request, self.get_data(search_value), search_value)

    def post(self, request):
        if "search" == request.POST.get('action', ''):
            search_value = request.POST.get('valor', '')
        else:
            search_value = ParametroUsuario.get_valor(
                request.user, 'basic_search', 'vp_rep_v_psto')
        return self.base_render(
            request, self.get_data(search_value), search_value)


class ReporteGraficaDPuesto(GenericList):
    html_template = template_base_path("gp")
    titulo = "Gráfica de Puesto"
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

    def base_render(self, request, data, search_value):
        ParametroUsuario.set_valor(
                request.user, 'basic_search', 'vp_rep_gr_psto', search_value)
        data = [{
            'puesto': reg.puesto,
            'puntos': float(f'{reg.ponderacion_total:0.2f}'),
            'pesos': float(f'{reg.ponderacion_total_en_pesos:0.2f}'),
        } for reg in data]
        return render(request, self.html_template, {
            'titulo': self.titulo,
            'titulo_descripcion': self.titulo_descripcion,
            'toolbar': [{'type': 'search'}],
            'footer': False,
            'read_only': False,
            'alertas': [],
            'req_chart': True,
            'search_value': search_value,
            'data': json.dumps(data),
            'tereapp': self.tereapp,
        })

    def get(self, request):
        search_value = ParametroUsuario.get_valor(
            request.user, 'basic_search', 'vp_rep_gr_psto')
        return self.base_render(
            request, self.get_data(search_value), search_value)

    def post(self, request):
        if "search" == request.POST.get('action', ''):
            search_value = request.POST.get('valor', '')
        else:
            search_value = ParametroUsuario.get_valor(
                request.user, 'basic_search', 'vp_rep_gr_psto')
        return self.base_render(
            request, self.get_data(search_value), search_value)

class ReporteGraficaDPuestoPesos(GenericList):
    html_template = template_base_path("gp_pesos")
    titulo = "Gráfica de Puesto"
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

    def base_render(self, request, data, search_value):
        ParametroUsuario.set_valor(
                request.user, 'basic_search', 'vp_rep_gr_psto', search_value)
        data = [{
            'puesto': reg.puesto,
            'puntos': float(f'{reg.ponderacion_total:0.2f}'),
            'pesos': float(f'{reg.ponderacion_total_en_pesos:0.2f}'),
        } for reg in data]
        return render(request, self.html_template, {
            'titulo': self.titulo,
            'titulo_descripcion': self.titulo_descripcion,
            'toolbar': [{'type': 'search'}],
            'footer': False,
            'read_only': False,
            'alertas': [],
            'req_chart': True,
            'search_value': search_value,
            'data': json.dumps(data),
            'tereapp': self.tereapp,
        })

    def get(self, request):
        search_value = ParametroUsuario.get_valor(
            request.user, 'basic_search', 'vp_rep_gr_psto')
        return self.base_render(
            request, self.get_data(search_value), search_value)

    def post(self, request):
        if "search" == request.POST.get('action', ''):
            search_value = request.POST.get('valor', '')
        else:
            search_value = ParametroUsuario.get_valor(
                request.user, 'basic_search', 'vp_rep_gr_psto')
        return self.base_render(
            request, self.get_data(search_value), search_value)
