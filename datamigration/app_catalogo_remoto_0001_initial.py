from django.contrib.auth.models import Permission

from zend_django.parametros_models import PARAM_TYPES
from zend_django.models import MenuOpc
from zend_django.models import ParametroUsuario

from .utils import update_permisos


def migration():
    update_permisos()

    opc = MenuOpc.objects.get_or_create(
        nombre="Catalogos Remotos",
        vista="catalogoremotoconfiguracion_list",
        posicion=8,
        padre=MenuOpc.objects.get(
            nombre='Administrar', vista='idx_tereapp_administracion')
    )[0]
    opc.permisos_requeridos.set([
        Permission.objects.get(codename='add_catalogoremotoconfiguracion'),
        Permission.objects.get(codename='change_catalogoremotoconfiguracion'),
        Permission.objects.get(codename='delete_catalogoremotoconfiguracion'),
        Permission.objects.get(codename='view_catalogoremotoconfiguracion'),
    ])

    ParametroUsuario.objects.get_or_create(
        seccion='basic_search', nombre='catalogoremotoconfiguracion',
        tipo=PARAM_TYPES['CADENA'], es_multiple=False)

    opc = MenuOpc.objects.get_or_create(
        nombre="Docu",
        vista="idx_app_catalogo_remoto",
        posicion=3
    )[0]
