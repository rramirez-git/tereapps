from django.contrib.auth.models import Permission

from app_valuacion_puestos.models import Tabulador
from app_valuacion_puestos.models import TabuladorNivel
from zend_django.models import MenuOpc
from zend_django.models import ParametroUsuario
from zend_django.parametros_models import PARAM_TYPES


def migration():
    vp = MenuOpc.objects.get_or_create(
        nombre="Valuacion de Puestos", posicion=1,
        padre=None, vista='idx_tereapp_valuacion_de_puestos')[0]
    items = {}
    items['tabulador'] = MenuOpc.objects.get_or_create(
        nombre="Tabuladores", posicion=4, padre=vp, vista="tabulador_list")[0]

    for obj, mnuOpc in items.items():
        ParametroUsuario.objects.get_or_create(
            seccion='basic_search', nombre=obj, valor_default='',
            tipo=PARAM_TYPES['CADENA'], es_multiple=False)
        mnuOpc.permisos_requeridos.set([
            Permission.objects.get(codename=f"add_{obj}"),
            Permission.objects.get(codename=f"change_{obj}"),
            Permission.objects.get(codename=f"delete_{obj}"),
            Permission.objects.get(codename=f"view_{obj}"),
        ])

    tab = Tabulador.objects.get_or_create(tabulador="1er Nivel")[0]
    TabuladorNivel.objects.get_or_create(
        tabulador=tab, posicion=1, porcentaje=100)

    tab = Tabulador.objects.get_or_create(tabulador="2do Nivel")[0]
    TabuladorNivel.objects.get_or_create(
        tabulador=tab, posicion=1, porcentaje=92)
    TabuladorNivel.objects.get_or_create(
        tabulador=tab, posicion=2, porcentaje=97)
    TabuladorNivel.objects.get_or_create(
        tabulador=tab, posicion=3, porcentaje=102)

    tab = Tabulador.objects.get_or_create(tabulador="3er Nivel")[0]
    TabuladorNivel.objects.get_or_create(
        tabulador=tab, posicion=1, porcentaje=85)
    TabuladorNivel.objects.get_or_create(
        tabulador=tab, posicion=2, porcentaje=90)
    TabuladorNivel.objects.get_or_create(
        tabulador=tab, posicion=3, porcentaje=95)
    TabuladorNivel.objects.get_or_create(
        tabulador=tab, posicion=4, porcentaje=100)
    TabuladorNivel.objects.get_or_create(
        tabulador=tab, posicion=5, porcentaje=105)
