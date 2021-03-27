from zend_django.models import *


def migration():

    mnuOpc = MenuOpc.objects.get(nombre="Configuracion", vista="")
    mnuOpc.vista = "idx_tereapp_configuracion"
    mnuOpc.save()

    mnuOpc = MenuOpc.objects.get(nombre="Adminstrar", vista="", padre=mnuOpc)
    mnuOpc.nombre = "Administrar"
    mnuOpc.vista = "idx_tereapp_administracion"
    mnuOpc.padre = None
    mnuOpc.posicion = 1001
    mnuOpc.save()
