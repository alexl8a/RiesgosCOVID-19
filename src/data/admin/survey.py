from django.contrib import admin
from django.utils.translation import gettext as _
from import_export.admin import ImportExportModelAdmin

from data.models import Survey


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


class SurveyAdmin(ImportExportModelAdmin, admin.ModelAdmin):

    list_display = [
        'name',
        'start_date',
        'end_date',
        'enabled',
    ]

    search_fields = [
        'name',
    ]

    readonly_fields = [
        'creation_date',
        'modified_date',
    ]

    list_filter = [
        'enabled',
    ]

    actions = [
        enable,
        disable,
    ]


admin.site.register(Survey, SurveyAdmin)
