from django.contrib.auth.views import (
    LoginView as BaseLoginView,
    PasswordChangeDoneView as BasePasswordChangeDoneView,
    PasswordChangeView as BasePasswordChange,
)
from django.urls import reverse_lazy

from users.auth.forms import AuthForm


class PasswordChangeView(BasePasswordChange):
    navtab = "change_password"
    template_name = "profile/change_password.html"
    success_url = reverse_lazy("users:password_change_done")


class PasswordChangeDoneView(BasePasswordChangeDoneView):
    navtab = "change_password"
    template_name = "profile/change_password_done.html"


class LoginViewCustom(BaseLoginView):
    template_name = "auth/login.html"
    authentication_form = AuthForm

    def post(self, request, *args, **kwargs):
        if not request.POST.get("remember_me", None):
            request.session.set_expiry(0)
        return super().post(request, *args, **kwargs)
