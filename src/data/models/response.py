from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext as _


class Response(models.Model):
    """ Response
    Refiera al una encuesta contestada
    """

    survey = models.ForeignKey(
        'data.Survey',
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name='responses',
        verbose_name=_('Encuesta'),
    )

    user = models.ForeignKey(
        get_user_model(),
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name='responses',
        verbose_name=_('Usuario'),
    )

    MEXICO = 1
    GUATEMALA = 2
    PANAMA = 3
    DOMINICANA = 4

    FACILITY_TYPES = (
        (MEXICO, _('México')),
        (GUATEMALA, _('Guatemala')),
        (PANAMA, _('Panamá')),
	    (DOMINICANA, _('República Dominicana'))
    )

    facility = models.IntegerField(
        null=False,
        blank=False,
        choices=FACILITY_TYPES,
        default=MEXICO,
        verbose_name=_('Sede'),
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

    expired_on = models.DateTimeField(
        null=False,
        blank=False,
        verbose_name=_('Fecha validez')
    )

    completion_date = models.DateTimeField(
        null=False,
        blank=False,
        verbose_name=_('Fecha completado')
    )

    enabled = models.BooleanField(
        null=False,
        default=True,
        verbose_name=_('¿Esta habilitado?')
    )

    creation_date = models.DateTimeField(auto_now_add=True)

    modified_date = models.DateTimeField(auto_now=True)

    @property
    def is_expired(self):
        return timezone.now() > self.expired_on
    
    @property
    def is_authorized(self):
        
        if self.risk_result_i > 150:
            return False
        
        if self.risk_result_v > 250:
            return False
        
        return True

    def __str__(self):
        return '{} {} {}'.format(
            self.survey,
            self.user,
            self.completion_date,
        )

    class Meta:

        verbose_name = _('Respuesta')

        verbose_name_plural = _('Respuestas')

        ordering = ('-completion_date',)
