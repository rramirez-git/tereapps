from django.contrib.auth.models import Permission
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType

from zend_django.models import *
from zend_django.parametros_models import PARAM_TYPES


def migration():
    ParametroUsuario.objects.get_or_create(
        seccion='general',
        nombre='open_left_menu',
        tipo=PARAM_TYPES['CADENA'],
        valor_default='True'
    )
