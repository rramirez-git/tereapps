"""
Definición de modelos para el Catalogo Remoto

Modelos
-------
- CatalogoRemoto => Catalogo Remoto
- Items => Elementos sincronizados del Catalogo Remoto
"""
from typing import Any, Iterable
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.urls import reverse
from django.utils.text import slugify

from zend_django.models import MenuOpc, ParametroUsuario
from zend_django.parametros_models import PARAM_TYPES


class CatalogoRemotoConfiguracion(models.Model):
    """
    Modelo de la Configuración Catalogo Remoto
    """
    nombre = models.CharField(max_length=250)
    url_script_sitio = models.URLField(
        help_text="https://teresita.com.mx/cmd.php?", max_length=500)
    comando_listar = models.CharField(
        max_length=250, help_text="&cmd=ls&")
    comando_mostrar = models.CharField(
        max_length=250, help_text="&cmd=show&")
    raiz_de_listado = models.CharField(
        max_length=250, help_text="&root=sie/Docu/Masters%20MP&")
    ruta_movil_de_archivo = models.CharField(
        max_length=250, help_text="&endpoint= -> &endpoint=ACE/ACE01/ACE01-005.png")
    elemento_thumbnail = models.CharField(
        max_length=250, help_text="&thumbnail=true&width=50")
    elementos_por_fila = models.PositiveSmallIntegerField(default=5)

    @property
    def url_list(self):
        return CatalogoRemotoConfiguracion.check_url_form(
            self.url_script_sitio + '?' +
            self.comando_listar + "&" +
            self.raiz_de_listado
        )

    def save(self, *args, **kwars):
        res = super().save(*args, **kwars)
        pk = self.pk
        mnu_padre = MenuOpc.objects.get(
            nombre="Docu", vista="idx_app_catalogo_remoto")
        mnu_opc = MenuOpc.objects.get_or_create(
            vista=f'catalogoremotoconfiguracion_display_{pk}',
            padre=mnu_padre, posicion=1)[0]
        mnu_opc.nombre = self.nombre
        mnu_opc.save()
        perm = Permission.objects.get_or_create(
            content_type=ContentType.objects.get(
                app_label='app_catalogo_remoto',
                model='catalogoremotoconfiguracion'),
            codename=f'view_catalogoremotoconfiguracion_{pk}'
            )[0]
        perm.name = f'Ver Catalogo Remoto {self.nombre}'
        perm.save()
        mnu_opc.permisos_requeridos.add(perm)

        return res

    def delete(self, *args, **kwars):
        pk = self.pk
        res = super().delete(*args, **kwars)
        MenuOpc.objects.get(
            nombre=self.nombre,
            vista=f'catalogoremotoconfiguracion_display_{pk}').delete()
        Permission.objects.get(
            codename=f'view_catalogoremotoconfiguracion_{pk}'
            ).delete()
        return res

    class Meta:
        ordering = ["nombre"]
        permissions = [
            ('synchronize_remote_catalogs', 'Sincronizar catalogos remotos'),
        ]

    def __str__(self) -> str:
        return f"{self.nombre}"

    @staticmethod
    def check_url_form(url: str) -> str:
        replacements = ((r'&&', '&'), (r'??', '?'), (r'?&', '?'), (r'&/', '/'))
        for old, new in replacements:
            while old in url:
                url = url.replace(old, new)
        return url[:-1] if url[-1] == "&" else url

class CatalogoRemoto(models.Model):
    """
    Modelo del Catalogo Remoto
    """
    nombre = models.CharField(max_length=250)
    url_listado_raiz = models.URLField(max_length=500)
    configuracion = models.ForeignKey(
        CatalogoRemotoConfiguracion, on_delete=models.CASCADE,
        related_name='catalogos')

    class Meta:
        ordering = ["nombre"]

    def __str__(self) -> str:
        return f"{self.nombre}"

    def create_parametro_usuario(self):
        if self.pk:
            return ParametroUsuario.objects.get_or_create(
                seccion='basic_search', nombre=f'catalogoremoto_{self.pk}',
                tipo=PARAM_TYPES['CADENA'], es_multiple=False)[0]

    def delete_parametro_usuario(self):
        if self.pk:
            return ParametroUsuario.objects.get_or_create(
                seccion='basic_search', nombre=f'catalogoremoto_{self.pk}',
                tipo=PARAM_TYPES['CADENA'], es_multiple=False)[0].delete()


    def save(self, *args, **kwars):
        res = super().save(*args, **kwars)
        self.create_parametro_usuario()
        return res

    def delete(self, *args, **kwars):
        self.delete_parametro_usuario()
        res = super().delete(*args, **kwars)
        return res

class Item(models.Model):
    """
    Modelo de los elementos del Catalogo Remoto
    """
    catalogo = models.ForeignKey(
        CatalogoRemoto, on_delete=models.CASCADE, related_name="items")
    nombre = models.TextField(max_length=250)
    mimetype = models.TextField(max_length=100)
    url = models.URLField(max_length=500)
    url_thumbnail = models.URLField(max_length=500)

    class Meta:
        ordering = ["nombre"]

    def __str__(self) -> str:
        return f"{self.nombre}"

    @property
    def as_filename(self):
        return slugify(f"{self}") + "." + self.url.split('.')[-1]
