from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _

class AuthForm(AuthenticationForm):
    remember_me = forms.BooleanField(initial=True, required=False, label=_("Remember me"))

    def clean_username(self):
        return self.cleaned_data["username"].lower()
