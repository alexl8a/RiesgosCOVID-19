from django.db import models
from django.utils.translation import gettext as _


class Survey(models.Model):

    name = models.CharField(
        max_length=300,
        null=False,
        blank=False,
        verbose_name=_('Nombre'),
    )

    description = models.CharField(
        max_length=500,
        null=True,
        blank=True,
        default=None,
        verbose_name=_('Descripción'),
    )

    start_date = models.DateTimeField(
        null=False,
        blank=False,
        verbose_name=_('Fecha de inicio')
    )

    end_date = models.DateTimeField(
        null=False,
        blank=False,
        verbose_name=_('Fecha de fin')
    )

    enabled = models.BooleanField(
        null=False,
        default=True,
        verbose_name=_('¿Esta habilitado?')
    )

    creation_date = models.DateTimeField(auto_now_add=True)

    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:

        verbose_name = _('Encuesta')

        verbose_name_plural = _('Encuestas')

        ordering = ('-id',)
