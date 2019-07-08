from django.http import HttpResponseRedirect
from django.urls import include, path, reverse_lazy
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", lambda r: HttpResponseRedirect(reverse_lazy("monitoring:list"))),
    path("monitoring/", ("monitoring.urls", "monitoring", "monitoring")),
    path("users/", ("users.urls", "users", "users")),

]
