"""
URL's para acceso a vista de la aplicacion app_nota

base_path => '/'

"""
from django.contrib.auth.decorators import login_required
from django.urls import include
from django.urls import path

from .views import CatalogosRemotosView

urlpatterns = [
     path(
          'catalogos-remotos/',
          login_required(CatalogosRemotosView.as_view()),
          name="idx_app_catalogo_remoto"),
     path('catalogo-remoto/',
          include('app_catalogo_remoto.catalogo.urls')),
     path('lista-catalogo-remoto/',
          include('app_catalogo_remoto.lista.urls')),
]
