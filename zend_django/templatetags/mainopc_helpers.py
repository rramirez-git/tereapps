"""
Funciones de ayuda para la generación, automaticación y correcta ejecución
del menú principal y sus opciones

Cargar con {% load mainopc_helpers %}
"""
from django import template
from django.contrib.auth.models import AnonymousUser
from django.contrib.auth.models import User
import json

from zend_django.menuopc_models import MenuOpc

register = template.Library()


@register.inclusion_tag(
    'zend_django/menuopc/list_opc.html', takes_context=True)
def print_menu_opc_adm(context, perms, opcion, nivel=-1):
    """
    Inclusion tag: {% print_menu_opc_adm perms opcion nivel %}
    Genera las etiquetas para generar el árbol de permisos con sangrias

    Parameters
    ----------
    context : ContextRequest
    perms : ContextRequest.perms
    opcion : MenuOpc
    nivel : int [-1]

    Returns
    -------
    dict
        Diccionario con las claves
            'nivel': int
            'reg': MenuOpc
            'perms': context[perms]
    """
    nivel += 1
    return {
        'nivel': nivel, 'reg': opcion, 'perms': perms
    }


def getMnuOpc4TereApp(tereapp):
    with open('managed/tereapps.json', 'r') as json_file:
        config = json.load(json_file)
    return MenuOpc.objects.get(padre=None, posicion=config[tereapp]['mnuopc_position'])


@register.simple_tag
def get_tereapp_name(tereapp=None):
    if "" == tereapp or tereapp is None:
        return ""
    return getMnuOpc4TereApp(tereapp).nombre


@register.inclusion_tag(
    'zend_django/menuopc/main_menu_opc.html', takes_context=True)
def main_menu(context, opciones=None, nivel=0, user_id=0, tereapp=None):
    """
    Inclusion tag: {% main_menu opciones nivel user_id %}
    Genera las etiquetas para generar el menú principal en la barra superior

    Parameters
    ----------
    context : ContextRequest
    opciones : array_like MenuOpc
    nivel : int [0]
    user_id : int [0] User.pk
    tereapp: string

    Returns
    -------
    dict
        Diccionario con las claves
            'nivel': int
            'opciones': array_like MenuOpc
            'user_id': int
            'tereapp'
    """
    user = context.get('user')
    if user is None:
        user = user_id if isinstance(
            user_id, User) else User.objects.get(pk=user_id)
    if nivel == 0 and isinstance(user, AnonymousUser):
        return {}
    if opciones is None:
        if "" == tereapp or tereapp is None:
            opciones = []
        else:
            with open('managed/tereapps.json', 'r') as json_file:
                config = json.load(json_file)
            mnuOpc = MenuOpc.objects.get(padre=None, posicion=config[tereapp]['mnuopc_position'])
            opciones = list(MenuOpc.objects.filter(padre=mnuOpc))
        nivel = 1
    else:
        nivel += 1
    opcs = []
    for opc in opciones:
        if opc.user_has_option(user):
            opcs.append(opc)
    return {
        'nivel': nivel, 'opciones': opcs, 'user_id': user.pk, 'tereapp': tereapp
    }

@register.inclusion_tag(
    'zend_django/menuopc/get_tereapps.html', takes_context=True)
def get_tereapps(context, user_id=0):
    """
    Inclusion tag: {% get_tereapps %}
    Genera las etiquetas para generar el menú de TereApps con base en las
    opciones de permisos en el menú principal
    Las opciones del menú en nivel 1 son las TereApps

    Parameters
    ----------
    context : ContextRequest
    user_id : int [0] User.pk

    Returns
    -------
    dict
        Diccionario con las claves
            'tereapps': array_like MenuOpc de nivel 1 correspondientes a las TereApps
    """
    user = context.get('user')
    if user is None:
        user = user_id if isinstance(
            user_id, User) else User.objects.get(pk=user_id)
    if isinstance(user, AnonymousUser):
        return {}
    with open('managed/tereapps.json', 'r') as json_file:
        config = json.load(json_file)
    opciones = []
    for key,configApp in config.items():
        print(configApp)
        if configApp['display_as_app'] != hid:
            opciones.append(MenuOpc.objects.get(
                padre=None, posicion=configApp['mnuopc_position']))
    return {
        'tereapps': [opc for opc in opciones if opc.user_has_option(user)],
    }

@register.inclusion_tag(
    'zend_django/menuopc/get_tereapps.html', takes_context=True)
def get_tereapps(context, user_id=0):
    """
    Inclusion tag: {% get_tereapps %}
    Genera las etiquetas para generar el menú de TereApps con base en las
    opciones de permisos en el menú principal
    Las opciones del menú en nivel 1 son las TereApps

    Parameters
    ----------
    context : ContextRequest
    user_id : int [0] User.pk

    Returns
    -------
    dict
        Diccionario con las claves
            'tereapps': array_like MenuOpc de nivel 1 correspondientes a las TereApps
    """
    user = context.get('user')
    if user is None:
        user = user_id if isinstance(
            user_id, User) else User.objects.get(pk=user_id)
    if isinstance(user, AnonymousUser):
        return {}
    with open('managed/tereapps.json', 'r') as json_file:
        config = json.load(json_file)
    opciones = []
    for key,configApp in config.items():
        if configApp['display_as_app']:
            opciones.append(MenuOpc.objects.get(
                padre=None, posicion=configApp['mnuopc_position']))
    return {
        'tereapps': [opc for opc in opciones if opc.user_has_option(user)],
    }

@register.inclusion_tag(
    'zend_django/menuopc/get_tereapps_hidden.html', takes_context=True)
def get_hidden_tereapps(context, user_id=0):
    user = context.get('user')
    if user is None:
        user = user_id if isinstance(
            user_id, User) else User.objects.get(pk=user_id)
    if isinstance(user, AnonymousUser):
        return {}
    with open('managed/tereapps.json', 'r') as json_file:
        config = json.load(json_file)
    opciones = []
    for key, configApp in config.items():
        if not configApp['display_as_app']:
            opciones.append(MenuOpc.objects.get(
                padre=None, posicion=configApp['mnuopc_position']))
    return  {
        'tereapps': [opc for opc in opciones if opc.user_has_option(user)],
    }
