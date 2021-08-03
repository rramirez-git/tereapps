"""
Definición de modelos para Tableros
"""
from django.db import models
from django.contrib.auth.models import Permission, ContentType
from zend_django.models import MenuOpc


class Tablero(models.Model):
    nombre = models.CharField(max_length=50)
    nombre_de_archivo = models.CharField(max_length=50)
    cuentas_base = models.CharField(max_length=200, default='')
    cuenta_ventas_netas = models.CharField(max_length=10, default='40000')

    __root_acc_nmb = []
    __root_acc = []
    __anios = []

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

    @property
    def cuentas_raiz(self):
        if len(self.__root_acc_nmb) == 0:
            self.__root_acc_nmb = [
                cta.strip() for cta in self.cuentas_base.split(',')]
            self.__root_acc.clear()
        if len(self.__root_acc) == 0:
            for cta in self.__root_acc_nmb:
                if cta == '':
                    self.__root_acc.append(None)
                else:
                    cuenta = self.cuentas.filter(cuenta=cta, entidad='T')
                    if cuenta.exists():
                        self.__root_acc.append(cuenta[0])
        return self.__root_acc

    @property
    def anios(self):
        if len(self.__anios) == 0:
            cta = self.cuentas_raiz[0]
            self.__anios = [det.anio for det in cta.detalle_anual.all()]
            self.__anios.sort()
        return self.__anios

    @property
    def primer_anio(self):
        return self.anios[0]

    @property
    def ultimo_anio(self):
        return self.anios[-1]

    @property
    def cta_vta_neta(self):
        for cta in self.cuentas_raiz:
            if cta.cuenta == self.cuenta_ventas_netas:
                return cta

