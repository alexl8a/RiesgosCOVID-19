from django.contrib.auth import get_user_model, login
from django.shortcuts import redirect, render
from django.utils.translation import gettext as _
from django.views import View

from landingpage.forms import LoginForm

User = get_user_model()


class LandingPage(View):

    template_name = 'landingpage/landingpage.html'

    def get(self, request):

        if request.user.is_authenticated:
            return redirect('web:response_list')

        form = LoginForm()

        return render(
            request,
            self.template_name,
            {
                'form': form
            }
        )

    def post(self, request):

        if request.user.is_authenticated:
            return redirect('web:response_list')

        form = LoginForm(request.POST)

        if form.is_valid():

            email = form.cleaned_data.get('email')

            username = email.split('@')[0]

            user, created = User.objects.get_or_create(
                username=username,
                email=email,
            )

            if not user.is_staff and not user.is_superuser:

                login(
                    request,
                    user,
                    'django.contrib.auth.backends.ModelBackend',
                )

                return redirect('web:response_list')

            form.add_error(
                'email',
                _('Lo sentimos las cuentas de administración es obligatorio entrar mediante Google')
            )

        return render(
            request,
            self.template_name,
            {
                'form': form
            }
        )
