from .views import GenericTereAppRootView


class ConfiguracionView(GenericTereAppRootView):
    html_template = "zend_django/idx_empty.html"
    titulo = "Configuración"
    tereapp = 'configuracion'


class AdministracionView(GenericTereAppRootView):
    html_template = "zend_django/idx_empty.html"
    titulo = "Administración"
    tereapp = 'administrar'
