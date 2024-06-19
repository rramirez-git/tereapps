"""
Definicion de modelos para comentarios
"""
from django.contrib.auth.models import User
from django.db import models


class Comentario(models.Model):
    comentario = models.TextField()
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)
    objeto = models.CharField(max_length=20)
    objeto_tipo = models.CharField(max_length=20)
    usuario = models.ForeignKey(
        User,
        related_name='comentarios',
        on_delete=models.PROTECT)
    en_respuesta_a = models.ForeignKey(
        'Comentario',
        related_name='respuestas',
        on_delete=models.CASCADE,
        null=True
    )

    class Meta:
        ordering = ['-actualizado']

    def __str__(self):
        return f"{self.comentario} ({self.usuario} - {self.actualizado})"
