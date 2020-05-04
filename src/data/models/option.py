from django.db import models
from django.utils.translation import gettext as _


class Option(models.Model):

    question = models.ForeignKey(
        'data.Question',
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name='options',
        verbose_name=_('Pregunta'),
    )

    order = models.IntegerField(
        null=False,
        blank=False,
        verbose_name=_('Orden')
    )

    text = models.CharField(
        max_length=300,
        null=False,
        blank=False,
        verbose_name=_('Texto')
    )

    risk_value_infection = models.IntegerField(
        null=False,
        blank=False,
        verbose_name=_('Valor de riesgo infección'),
    )

    risk_value_vulnerability = models.IntegerField(
        null=False,
        blank=False,
        verbose_name=_('Valor de riesgo vulnerabilidad'),
    )

    enabled = models.BooleanField(
        null=False,
        default=True,
        verbose_name=_('¿Esta habilitado?')
    )

    creation_date = models.DateTimeField(auto_now_add=True)

    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text

    class Meta:

        verbose_name = _('Opción')

        verbose_name_plural = _('Opciones')

        ordering = ('question', 'order')
