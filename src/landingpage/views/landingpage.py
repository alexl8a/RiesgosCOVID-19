from django.contrib.auth import get_user_model, login
from django.shortcuts import redirect, render
from django.utils.translation import gettext as _
from django.views import View

from landingpage.forms import LoginForm

User = get_user_model()


class LandingPage(View):

    template_name = 'landingpage/landingpage.html'

    def get(self, request):

        return render(
            request,
            self.template_name
        )

