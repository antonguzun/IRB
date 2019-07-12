from django.urls import path

from .views import MonitoringListView

urlpatterns = [
    path('list/', MonitoringListView.as_view(), name='list'),
]
