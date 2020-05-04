from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import redirect, render
from django.views import View

from data.models import Response


class Dashboard(PermissionRequiredMixin, View):

    permission_required = 'data.view_response'

    template_name = 'web/dashboard.html'

    def get(self, request):

        mexico_count_responses = Response.objects.filter(
            enabled=True,
            facility=Response.MEXICO,
        ).count()

        mexico_responses = Response.objects.filter(
            enabled=True,
            facility=Response.MEXICO,
        )[:50]

        guatemala_count_responses = Response.objects.filter(
            enabled=True,
            facility=Response.GUATEMALA,
        ).count()

        guatemala_responses = Response.objects.filter(
            enabled=True,
            facility=Response.GUATEMALA,
        )[:50]

        panama_count_responses = Response.objects.filter(
            enabled=True,
            facility=Response.PANAMA,
        ).count()

        panama_responses = Response.objects.filter(
            enabled=True,
            facility=Response.PANAMA,
        )[:50]

        dominicana_count_responses = Response.objects.filter(
            enabled=True,
            facility=Response.DOMINICANA,
        ).count()

        dominicana_responses = Response.objects.filter(
            enabled=True,
            facility=Response.DOMINICANA,
        )[:50]

        return render(
            request,
            self.template_name,
            {
                'mexico_count_responses': mexico_count_responses,
                'mexico_responses': mexico_responses,
                'guatemala_count_responses': guatemala_count_responses,                
                'guatemala_responses': guatemala_responses,
                'panama_count_responses': panama_count_responses,
                'panama_responses': panama_responses,
                'dominicana_count_responses': dominicana_count_responses,
                'dominicana_responses': dominicana_responses,
            }
        )
