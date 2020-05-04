from django.db import models
from django.utils.translation import gettext as _


class Question(models.Model):

    SINGLE_OPTION = 1
    SELECT_MULTIPLE = 2
    NUMBER = 3
    TEXT = 4

    QUESTION_TYPES = (
        (SINGLE_OPTION, _('Uníca')),
        (SELECT_MULTIPLE, _('Selección multiple')),
        (NUMBER, _('Numerica')),
	    (TEXT, _('Texto'))
    )

    survey = models.ForeignKey(
        'data.Survey',
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name='questions',
        verbose_name=_('Encuesta'),
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

    required = models.BooleanField(
        null=False,
        default=True,
        verbose_name=_('campo requerido')
    )

    question_type = models.IntegerField(
        null=False,
        blank=False,
        choices=QUESTION_TYPES,
        default=SINGLE_OPTION,
        verbose_name=_('Tipo'),
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

        verbose_name = _('Pregunta')

        verbose_name_plural = _('Preguntas')

        ordering = ('survey', 'order')
