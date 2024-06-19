from django.contrib.auth.models import Permission

from zend_django.menuopc_models import MenuOpc
from zend_django.parametros_models import ParametroSistema, PARAM_TYPES

from app_tablero.models import Tablero


def migration():
    mnu_main = MenuOpc.objects.get_or_create(
        nombre="Tableros Contables", posicion=2,
        padre=None, vista='idx_tereapp_tableros'
    )[0]

    mnu_tableros = MenuOpc.objects.get_or_create(
        nombre="Tableros", posicion=1,
        padre=mnu_main, vista='tablero_list'
    )[0]

    mnu_load = MenuOpc.objects.get_or_create(
        nombre="Carga Automatica", posicion=2,
        padre=mnu_main, vista='auto_load_tableros'
    )[0]

    mnu_tableros.permisos_requeridos.set([
        Permission.objects.get(codename=f'{perm}_{elem}')
        for elem in ['tablero', 'cuenta', 'estadistico']
        for perm in ['add', 'change', 'delete', 'view']])

    mnu_load.permisos_requeridos.set([
        Permission.objects.get(codename=f'add_estadistico')
    ])

    ParametroSistema.objects.get_or_create(
        seccion='AppTablero',
        nombre='ruta_abs_ftp',
        nombre_para_mostrar='Ruta absoluta FTP',
        tipo=PARAM_TYPES['CADENA'],
        es_multiple=False,
    )

    cuentas_base = '41100,41200,40000,50000,59000,61100,62100,63100,64100,'
    cuentas_base += '66100,60000,80000'
    Tablero.objects.get_or_create(
        nombre='Elasticintas Teresita',
        nombre_de_archivo='ET-Tablero-Contabilidad.xlsm',
        cuentas_base=cuentas_base)

    cuentas_base = '40000,51100,,63000,61100,62100,63300,63400,63500,63600,'
    cuentas_base += '63700,64100,65100'
    Tablero.objects.get_or_create(
        nombre='Genyka',
        nombre_de_archivo='Genyka-Tablero-Contabilidad.xlsm',
        cuentas_base=cuentas_base)
