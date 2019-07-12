from django.views.generic import ListView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import DevicesState

class MonitoringListView(LoginRequiredMixin, ListView):
    login_url = '/users/login/'
    redirect_field_name = 'redirect_to'
    template_name = "monitoring_list.html"
    model = DevicesState
    ordering = "-id"
