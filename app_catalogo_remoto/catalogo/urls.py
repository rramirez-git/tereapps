"""
URL's para el modulo de administración de Catalogos Remotos
Se generan las url para CRUD con los permisos requeridos

obj = 'catalogoremotoconfiguracion'
app_label = 'app_catalogo_remoto'

base_path => catalogo-remoto/

Perm => View => Path
--------------------
- view   => list   =>
- add    => create => nuevo/
- change => update => actualizar/<pk>/
- delete => delete => eliminar/<pk>/
- view   => read   => <pk>/

permiso_requerido = {app_label}.{Perm}_{obj}
vista = {obj}_{View}

"""
from django.contrib.auth.decorators import permission_required, login_required
from django.urls import path

import app_catalogo_remoto.catalogo.vw as views

from .models import CatalogoRemotoConfiguracion

obj = 'catalogoremotoconfiguracion'
app_label = 'app_catalogo_remoto'

urlpatterns = [
    path('', permission_required(
        f'{app_label}.view_{obj}')(views.List.as_view()),
        name=f"{obj}_list"),
    path('nuevo/', permission_required(
        f'{app_label}.add_{obj}')(views.Create.as_view()),
        name=f"{obj}_create"),
    path('actualizar/<pk>/', permission_required(
        f'{app_label}.change_{obj}')(views.Update.as_view()),
        name=f"{obj}_update"),
    path('eliminar/<pk>/', permission_required(
        f'{app_label}.delete_{obj}')(views.Delete.as_view()),
        name=f"{obj}_delete"),
    path('sincronizar/<pk>/', permission_required(
        f'{app_label}.synchronize_remote_catalogs')(
            views.Sincronizar.as_view()),
        name=f"{obj}_sinchronize"),
    path('<pk>/', permission_required(
        f'{app_label}.view_{obj}')(views.Read.as_view()),
        name=f"{obj}_read"),
    path(f'mostrar/<pk>/', login_required()(views.Display.as_view()),
        name=f"{obj}_display"),
    path(f'detalle/<pk>/', login_required()(views.DisplayItems.as_view()),
        name=f"{obj}_display_detail"),
    path('eliminar-item/<pk>/', permission_required(
        f'{app_label}.delete_{obj}')(views.DeleteItem.as_view()),
        name=f"{obj}_delete_item"),
    path('eliminar-catalogo/<pk>/', permission_required(
        f'{app_label}.delete_{obj}')(views.DeleteCatalogo.as_view()),
        name=f"{obj}_delete_catalogo"),
    path('catalogo/<pk>/', permission_required(
        f'{app_label}.view_{obj}')(views.ReadCatalogo.as_view()),
        name=f"{obj}_read_catalogo"),
] + [
    path(f'mostrar/{crc.pk}/', permission_required(
        f'{app_label}.view_{obj}_{crc.pk}')(views.Display.as_view()),
        name=f"{obj}_display_{crc.pk}")
    for crc in CatalogoRemotoConfiguracion.objects.all()
    ]
