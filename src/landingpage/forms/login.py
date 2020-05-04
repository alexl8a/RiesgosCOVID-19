from captcha.fields import ReCaptchaField
from django import forms
from django.utils.translation import gettext as _


class LoginForm(forms.Form):

    email = forms.EmailField(
        required=True,
        label=_('Correo electrónico')
    )

    captcha = ReCaptchaField(
        required=True,
    )
