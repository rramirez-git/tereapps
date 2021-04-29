from django.contrib.auth.models import Permission

from zend_django.models import MenuOpc
from zend_django.models import ParametroUsuario
from zend_django.parametros_models import PARAM_TYPES

from app_valuacion_puestos.models import ParametroVP

def migration():
    vp = MenuOpc.objects.get_or_create(
        nombre="Valuacion de Puestos", posicion=1,
        padre=None, vista='idx_tereapp_valuacion_de_puestos')[0]

    opc_rep = MenuOpc.objects.get_or_create(
        nombre="Reportes", posicion=5,
        padre=vp)[0]

    MenuOpc.objects.get_or_create(
        nombre='Factores por Puesto', posicion=1,
        padre=opc_rep, vista='app_vp_rep_fp_ptos')[0].permisos_requeridos.set([
        Permission.objects.get(codename=f"view_fp_puntos"),
        Permission.objects.get(codename=f"view_fp_niveles"),])
    MenuOpc.objects.get_or_create(
        nombre='Valor por Puesto', posicion=2,
        padre=opc_rep, vista='app_vp_rep_vp')[0].permisos_requeridos.set([
        Permission.objects.get(codename=f"view_vp"),])
    MenuOpc.objects.get_or_create(
        nombre='Grafica de Puesto', posicion=3,
        padre=opc_rep, vista='app_vp_rep_gp')[0].permisos_requeridos.set([
        Permission.objects.get(codename=f"view_gp"),])

    ParametroUsuario.objects.get_or_create(
        seccion='basic_search', nombre='vp_rep_f_psto_ptos',
        valor_default='',
        tipo=PARAM_TYPES['CADENA'], es_multiple=False)
    ParametroUsuario.objects.get_or_create(
        seccion='basic_search', nombre='vp_rep_f_psto_nvl',
        valor_default='',
        tipo=PARAM_TYPES['CADENA'], es_multiple=False)
    ParametroUsuario.objects.get_or_create(
        seccion='basic_search', nombre='vp_rep_v_psto',
        valor_default='',
        tipo=PARAM_TYPES['CADENA'], es_multiple=False)
    ParametroUsuario.objects.get_or_create(
        seccion='basic_search', nombre='vp_rep_gr_psto',
        valor_default='',
        tipo=PARAM_TYPES['CADENA'], es_multiple=False)

    ParametroVP.objects.get_or_create(parametro="DiasPorMes", valor=30)
