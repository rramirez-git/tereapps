"""
URL's para acceso a vista de la aplicacion app_valuacion_puestos

base_path =>
"""
from django.contrib.auth.decorators import login_required, permission_required
from django.urls import include
from django.urls import path

import app_valuacion_puestos.app_vw as views


app_label = 'app_valuacion_puestos'

urlpatterns = [
    path('valuacion-de-puestos',
         login_required(views.ValuacionPuestosView.as_view()),
         name="idx_tereapp_valuacion_de_puestos"),

    path('puesto/', include('app_valuacion_puestos.puesto_urls')),
    path('factor/', include('app_valuacion_puestos.factor_urls')),
    path('nivel/', include('app_valuacion_puestos.nivel_urls')),
    path('parametrovp/', include('app_valuacion_puestos.parametrovp_urls')),
    path('tabulador/', include('app_valuacion_puestos.tabulador_urls')),
    path('nivel-de-tabulador/', include('app_valuacion_puestos.tabuladornivel_urls')),

    path('factor-por-puesto-puntos/',
         permission_required(f'{app_label}.view_fp_puntos')(
             views.ReporteFactPPuestoPtos.as_view()),
         name='app_vp_rep_fp_ptos'),
    path('factor-por-puesto-niveles/',
         permission_required(f'{app_label}.view_fp_niveles')(
             views.ReporteFactPPuestoNiveles.as_view()),
         name='app_vp_rep_fp_niveles'),
    path('valor-por-puesto/',
         permission_required(f'{app_label}.view_vp')(
             views.ReporteValorPPuesto.as_view()),
         name='app_vp_rep_vp'),
    path('grafica-de-puestos/',
         permission_required(f'{app_label}.view_gp')(
             views.ReporteGraficaDPuesto.as_view()),
         name='app_vp_rep_gp'),
    path('grafica-de-puestos-pesos/',
         permission_required(f'{app_label}.view_gp_pesos')(
             views.ReporteGraficaDPuestoPesos.as_view()),
         name='app_vp_rep_gp_pesos'),
]
