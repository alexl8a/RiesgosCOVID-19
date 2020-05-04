from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, render
from django.views import View

from data import models


class ResponseDetail(LoginRequiredMixin, View):

    template_name = 'web/response_detail.html'

    def get(self, request, pk, **kwargs):

        response = get_object_or_404(
            models.Response,
            pk=pk,            
            enabled=True,
        )

        answers = response.answers.order_by('option')

        return render(
            request,
            self.template_name,
            {
                'response': response,
                'answers': answers
            }
        )
