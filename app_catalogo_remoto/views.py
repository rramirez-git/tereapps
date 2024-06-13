from zend_django.views import GenericTereAppRootView


class CatalogosRemotosView(GenericTereAppRootView):
    html_template = "zend_django/idx_empty.html"
    titulo = "Catálogos Remotos"
    titulo_descripcion = ""
    toolbar = None
    tereapp = 'catalogo_remoto'
