from django.contrib.auth.models import Permission

from zend_django.models import MenuOpc
from zend_django.models import ParametroUsuario
from zend_django.parametros_models import PARAM_TYPES

from .utils import update_permisos


def migration():
    update_permisos()

    opc = MenuOpc.objects.get_or_create(
        nombre="Listas de Catalogos Remotos",
        vista="listacatalogo_list",
        posicion=9,
        padre=MenuOpc.objects.get(
            nombre='Administrar', vista='idx_tereapp_administracion')
    )[0]
    opc.permisos_requeridos.set([
        Permission.objects.get(codename='add_listacatalogo'),
        Permission.objects.get(codename='change_listacatalogo'),
        Permission.objects.get(codename='delete_listacatalogo'),
        Permission.objects.get(codename='view_listacatalogo'),
    ])

    ParametroUsuario.objects.get_or_create(
        seccion='basic_search', nombre='listacatalogo',
        tipo=PARAM_TYPES['CADENA'], es_multiple=False)
