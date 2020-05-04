from django.contrib import admin
from django.utils.translation import gettext as _
from import_export.admin import ImportExportModelAdmin

from data.models import Response


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


class ResponseAdmin(ImportExportModelAdmin, admin.ModelAdmin):

    list_display = [
        'survey',
        'user',
        'facility',
        'risk_result_i',
        'risk_result_v',        
        'is_expired',
        'is_authorized',
    ]

    search_fields = [
        'survey__name',
        'user__email',
        'user__first_name',
        'user__last_name',
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


admin.site.register(Response, ResponseAdmin)
