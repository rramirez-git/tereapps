""""
URL's para acceso a vista de la aplicacion app_tablero

base_path =>
"""
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from django.urls import include
from django.urls import path

import app_tablero.app_vw as views


app_label = 'app_tablero'

urlpatterns = [
    path('tableros-contables/',
         login_required(views.TablerosView.as_view()),
         name='idx_tereapp_tableros'),

    path('carga-automatica-tableros-contables/',
         views.TablerosAutoLoadView.as_view(),
         name='auto_load_tableros'),

    path('tablero-contable/<pk>/',
         login_required(views.VerTablero.as_view()),
         name='ver_tablero_contable'),

    path('tablero/', include('app_tablero.tablero_urls')),
    path('cuenta/', include('app_tablero.cuenta_urls')),
    path('estadistico/', include('app_tablero.estadistico_urls')),
]
