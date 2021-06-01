from datetime import date
from django.contrib.auth.models import Permission

from app_valuacion_puestos.models import Factor
from app_valuacion_puestos.models import Nivel
from app_valuacion_puestos.models import ParametroVP
from app_valuacion_puestos.models import ParametroVPHistoria
from app_valuacion_puestos.models import Puesto
from zend_django.models import MenuOpc
from zend_django.models import ParametroUsuario
from zend_django.parametros_models import PARAM_TYPES


def migration():
    vp = MenuOpc.objects.get_or_create(
        nombre="Valuacion de Puestos", posicion=1,
        padre=None, vista='idx_tereapp_valuacion_de_puestos')[0]
    items = {}
    items['parametrovp'] = MenuOpc.objects.get_or_create(
        nombre="Parametros", posicion=3, padre=vp, vista="parametrovp_list")[0]

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

    exp5 = ParametroVP.objects.get_or_create(parametro="Exponente5N", valor=2.1)[0]
    exp6 = ParametroVP.objects.get_or_create(parametro="Exponente6N", valor=1.8104)[0]
    valpto = ParametroVP.objects.get_or_create(parametro="ValorPunto", valor=0.3792796)[0]
    ParametroVPHistoria.objects.get_or_create(
        raiz=exp5,
        parametro=exp5.parametro,
        valor=exp5.valor,
        fecha=exp5.fecha
    )
    ParametroVPHistoria.objects.get_or_create(
        raiz=exp6,
        parametro=exp6.parametro,
        valor=exp6.valor,
        fecha=exp6.fecha
    )
    ParametroVPHistoria.objects.get_or_create(
        raiz=valpto,
        parametro=valpto.parametro,
        valor=valpto.valor,
        fecha=valpto.fecha
    )
