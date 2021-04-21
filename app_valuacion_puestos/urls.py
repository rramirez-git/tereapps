"""
URL's para acceso a vista de la aplicacion app_valuacion_puestos

base_path =>
"""
from django.contrib.auth.decorators import login_required
from django.urls import include
from django.urls import path

from .app_vw import ValuacionPuestosView

urlpatterns = [
    path('valuacion-de-puestos',
         login_required(ValuacionPuestosView.as_view()),
         name="idx_tereapp_valuacion_de_puestos"),
    path('puesto/', include('app_valuacion_puestos.puesto_urls')),
    path('factor/', include('app_valuacion_puestos.factor_urls')),
    path('nivel/', include('app_valuacion_puestos.nivel_urls')),
    path('parametrovp/', include('app_valuacion_puestos.parametrovp_urls')),
    path('tabulador/', include('app_valuacion_puestos.tabulador_urls')),
    path('nivel-de-tabulador/', include('app_valuacion_puestos.tabuladornivel_urls')),
]
