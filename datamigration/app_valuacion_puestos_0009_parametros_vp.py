from app_valuacion_puestos.models import ParametroVP
from zend_django.parametros_models import PARAM_TYPES
from zend_django.parametros_models import ParametroSistema


def migration():
    ParametroSistema.objects.get_or_create(
        seccion='AppValuacionPuestos',
        nombre='DiasPorMes',
        nombre_para_mostrar='Días por Mes',
        valor=ParametroVP.objects.get(parametro='DiasPorMes').valor,
        tipo=PARAM_TYPES['DECIMAL'],
        es_multiple=False
    )
    ParametroSistema.objects.get_or_create(
        seccion='AppValuacionPuestos',
        nombre='Exponente5N',
        nombre_para_mostrar='Exponente 5 Niveles',
        valor=ParametroVP.objects.get(parametro='Exponente5N').valor,
        tipo=PARAM_TYPES['DECIMAL'],
        es_multiple=False
    )
    ParametroSistema.objects.get_or_create(
        seccion='AppValuacionPuestos',
        nombre='Exponente6N',
        nombre_para_mostrar='Exponente 6 Niveles',
        valor=ParametroVP.objects.get(parametro='Exponente6N').valor,
        tipo=PARAM_TYPES['DECIMAL'],
        es_multiple=False
    )

    ParametroVP.objects.get(parametro='DiasPorMes').delete()
    ParametroVP.objects.get(parametro='Exponente5N').delete()
    ParametroVP.objects.get(parametro='Exponente6N').delete()
