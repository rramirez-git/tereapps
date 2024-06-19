"""
Definición de modelos para el Catalogo Remoto

Modelos
-------
- ListaCatalogo => Catalogo Remoto
- ListaCatalogoItems => Elementos sincronizados del Catalogo Remoto
"""
from django.contrib.auth.models import User
from django.db import models

from app_catalogo_remoto.catalogo.models import Item


class ListaCatalogo(models.Model):
    nombre = models.CharField(max_length=250)
    usr = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='listas_catalogo')

    class Meta:
        ordering = ["nombre"]

    def __str__(self) -> str:
        return f"{self.nombre}"


class ListaCatalogoItem(models.Model):
    lista = models.ForeignKey(
        ListaCatalogo, on_delete=models.CASCADE, related_name='items')
    item = models.ForeignKey(
        Item, on_delete=models.CASCADE, related_name='listas')

    class Meta:
        ordering = ["lista__nombre", "item__nombre"]

    def __str__(self) -> str:
        return f"{self.item.nombre}"
