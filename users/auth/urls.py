from django.contrib.auth.views import LogoutView
from django.urls import path, reverse_lazy

from .views import LoginViewCustom

urlpatterns = [
    path("login/", LoginViewCustom.as_view(redirect_authenticated_user=True), name="login"),
    path("logout/", LogoutView.as_view(next_page=reverse_lazy("users:login")), name="logout"),
    #path("change_password/done/", PasswordChangeDoneView.as_view(), name="password_change_done"),
    #path("change_password/", PasswordChangeView.as_view(), name="change_password"),
]
