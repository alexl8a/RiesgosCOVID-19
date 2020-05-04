from django.contrib import admin
from django.utils.translation import gettext as _
from import_export.admin import ImportExportModelAdmin

from data.models import Question


def enable(modeladmin, request, queryset):

    queryset.update(enabled=True)


enable.short_description = _(
    'Habilitar',
)


def disable(modeladmin, request, queryset):

    queryset.update(enabled=False)


disable.short_description = _(
    'Inhabilitar',
)


class QuestionAdmin(ImportExportModelAdmin, admin.ModelAdmin):

    list_display = [
        'survey',
        'text',
        'enabled',
    ]

    search_fields = [
        'survey',
        'text',
    ]

    readonly_fields = [
        'creation_date',
        'modified_date',
    ]

    list_filter = [
        'question_type',
        'enabled',
    ]

    actions = [
        enable,
        disable,
    ]


admin.site.register(Question, QuestionAdmin)
