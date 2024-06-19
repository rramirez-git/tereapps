from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View

from zend_django.views import GenericCreate
from zend_django.views import GenericDelete
from zend_django.views import GenericList
from zend_django.views import GenericRead
from zend_django.views import GenericUpdate

from .forms import frmMain as base_form
from .models import ListaCatalogo as main_model
from .models import ListaCatalogoItem
from app_catalogo_remoto.catalogo.models import Item


def template_base_path(file):
    return 'app_catalogo_remoto/lista/' + file + ".html"


class List(GenericList):
    html_template = template_base_path("list")
    titulo = "Listas de Catalogos Remotos"
    main_data_model = main_model
    model_name = "listacatalogo"
    tereapp = 'administrar'

    def get_data(self, search_value=''):
        if '' == search_value:
            return list(
                self.main_data_model.objects.all())
        else:
            return list(self.main_data_model.objects.filter(
                Q(nombre__icontains=search_value) |
                Q(usr__first_name__icontains=search_value) |
                Q(usr__last_name__icontains=search_value) |
                Q(usr__profile__apellido_materno__icontains=search_value)))


class Read(GenericRead):
    titulo_descripcion = "lista de Catalogo Remoto"
    model_name = "listacatalogo"
    base_data_form = base_form
    main_data_model = main_model
    tereapp = 'administrar'
    # html_template = template_base_path("read")


class Create(GenericCreate):
    titulo = "Lista de Catalogo Remoto"
    model_name = "listacatalogo"
    base_data_form = base_form
    tereapp = 'administrar'


class Update(GenericUpdate):
    titulo = "Lista de Catalogo Remoto"
    model_name = "listacatalogo"
    base_data_form = base_form
    main_data_model = main_model
    tereapp = 'administrar'


class Delete(GenericDelete):
    model_name = "listacatalogo"
    main_data_model = main_model
    tereapp = 'administrar'


class AddCatalogItemToList(View):

    def post(self, request, pk):
        item = int('0' + request.POST.get('item', ''))
        list = int('0' + request.POST.get('list', ''))
        new_list = request.POST.get('new_list', '')
        if item > 0:
            item = Item.objects.get(pk=item)
            if list > 0:
                list = main_model.objects.get(pk=list)
                ListaCatalogoItem.objects.get_or_create(lista=list, item=item)
            if new_list:
                list = main_model.objects.get_or_create(
                    nombre=new_list, usr=request.user)[0]
                ListaCatalogoItem.objects.get_or_create(lista=list, item=item)
        return HttpResponseRedirect(reverse(
            'catalogoremotoconfiguracion_display_detail', kwargs={'pk': pk}))


class RemoveCatalogItemFromList(View):

    def post(self, request, pk):
        item = int('0' + request.POST.get('item', ''))
        if item > 0:
            ListaCatalogoItem.objects.get(pk=item).delete()
        return HttpResponseRedirect(reverse(
            'listacatalogo_display_detail', kwargs={'pk': pk}))


class DisplayItems(View):
    main_data_model = main_model
    tereapp = 'catalogo_remoto'
    html_template = template_base_path("display_items")

    def get(self, request, pk=None):
        if not self.main_data_model.objects.filter(pk=pk).exists():
            return HttpResponseRedirect(reverse('item_no_encontrado'))
        obj = self.main_data_model.objects.get(pk=pk)
        toolbar = None
        return render(request, self.html_template, {
            'titulo': obj,
            'toolbar': toolbar,
            'footer': False,
            'read_only': True,
            'alertas': [],
            'req_chart': False,
            'search_value': '',
            'tereapp': self.tereapp,
            'object': obj,
            'withoutBtnSave': True,
        })


class DeleteFromUsrDisplay(Delete):

    def get(self, request, pk):
        super().get(request, pk)
        return HttpResponseRedirect(reverse('idx_app_catalogo_remoto'))
