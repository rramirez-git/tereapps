from zend_django.models import ParametroSistema
from zend_django.parametros_models import PARAM_TYPES

def migration():

    ParametroSistema.objects.get_or_create(
        seccion="SitioGeneral",
        nombre="left_bar_width",
        nombre_para_mostrar="Ancho barra de menú (px)",
        valor="200",
        tipo=PARAM_TYPES['ENTERO'],
        es_multiple=False
    )

