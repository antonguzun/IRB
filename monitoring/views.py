from django.views.generic import ListView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class MonitoringListView(LoginRequiredMixin, TemplateView):
    login_url = '/users/login/'
    redirect_field_name = 'redirect_to'
    template_name = "monitoring_list.html"
