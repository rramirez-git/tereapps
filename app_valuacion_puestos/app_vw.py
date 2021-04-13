from zend_django.views import GenericTereAppRootView

class ValuacionPuestosView(GenericTereAppRootView):
    html_template = "zend_django/idx_empty.html"
    titulo = "Valuación de Puestos"
    tereapp = 'valuacion_de_puestos'
