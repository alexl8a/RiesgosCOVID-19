from django.db import models
from django.utils.translation import gettext as _


class Answer(models.Model):
    """ Answer
    Answer lo que contesto
    """
    response = models.ForeignKey(
        'data.Response',
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name='answers',
        verbose_name=_('Respuesta'),
    )

    option = models.ForeignKey(
        'data.Option',
        null=True,
        blank=True,
        default=None,
        on_delete=models.SET_NULL,
        related_name='answers',
        verbose_name=_('Opción'),
    )

    answer_value = models.CharField(
        max_length=300,
        null=True,
        blank=True,
        default=None,
        verbose_name=_('Valor')
    )

    risk_result_i = models.IntegerField(        
        null=False,
        blank=False,
        verbose_name=_('Resultado del riesgo infección'),
    )

    risk_result_v = models.IntegerField(        
        null=False,
        blank=False,
        verbose_name=_('Resultado del riesgo vulnerabilidad'),
    )

    enabled = models.BooleanField(
        null=False,
        default=True,
        verbose_name=_('¿Esta habilitado?')
    )

    creation_date = models.DateTimeField(auto_now_add=True)

    modified_date = models.DateTimeField(auto_now=True)

    class Meta:

        verbose_name = _('Opcion respondida')

        verbose_name_plural = _('Opciones respondidas')

        ordering = ('response', 'id')

    def __str__(self):
        return self.answer_value
