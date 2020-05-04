from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View

from data import models


class ResponseList(LoginRequiredMixin, View):

    template_name = 'web/response_list.html'

    def get(self, request):

        response = models.Response.objects.filter(
            enabled=True,
            user=request.user,
        ).order_by('-completion_date').first()

        if response is None or response.is_expired:

            return redirect('web:response_add')

        return render(request, self.template_name, {'response': response})
