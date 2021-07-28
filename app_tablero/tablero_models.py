"""
Definición de modelos para Tableros
"""
from django.db import models
from django.contrib.auth.models import Permission, ContentType
from zend_django.models import MenuOpc

class Tablero(models.Model):
    nombre = models.CharField(max_length=50)
    nombre_de_archivo = models.CharField(max_length=50)

    class Meta:
        ordering = ['nombre']

    def __str__(self):
        return self.nombre

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        ct = ContentType.objects.get(app_label='app_tablero', model='tablero')
        perm = Permission.objects.get_or_create(
            content_type=ct, codename=f'view_dashboard_{self.pk}')[0]
        perm.name = f'Ver Tablero {self.nombre}'
        perm.save()

    def delete(self, *args, **kwargs):
        ct = ContentType.objects.get(app_label='app_tablero', model='tablero')
        perm = Permission.objects.get_or_create(
            content_type=ct, codename=f'view_dashboard_{self.pk}')[0]
        perm.delete()
        super().delete(*args, **kwargs)

    def displayable2user(self, user):
        return user.has_perm(f'app_tablero.view_dashboard_{self.pk}')

