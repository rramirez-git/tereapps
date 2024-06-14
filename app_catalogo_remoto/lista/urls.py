"""
URL's para el modulo de administración de Catalogos Remotos
Se generan las url para CRUD con los permisos requeridos

obj = 'listacatalogo'
app_label = 'app_catalogo_remoto'

base_path => listas-catalogo-remoto/

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

import app_catalogo_remoto.lista.vw as views


obj = 'listacatalogo'
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

    path('agregar-item-a-lista/<pk>/', login_required()(
        views.AddCatalogItemToList.as_view()),
        name=f"{obj}_add_item"),
    path('eliminar-item-de-lista/<pk>/', login_required()(
        views.RemoveCatalogItemFromList.as_view()),
        name=f"{obj}_remove_item"),
    path(f'detalle/<pk>/', login_required()(views.DisplayItems.as_view()),
        name=f"{obj}_display_detail"),
    path('eliminar-lista/<pk>/', login_required()(
        views.DeleteFromUsrDisplay.as_view()),
        name=f"{obj}_remove_list"),

    path('<pk>/', permission_required(
        f'{app_label}.view_{obj}')(views.Read.as_view()),
        name=f"{obj}_read"),
]
