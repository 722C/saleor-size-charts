from django.conf.urls import url

from . import storefront_views
from .dashboard_views import views as dashboard_views

urlpatterns = [
    url(r'^dashboard/size-charts/$',
        dashboard_views.size_chart_list,
        name='size-chart-dashboard-list'),
    url(r'^dashboard/size-charts/create/$',
        dashboard_views.size_chart_create,
        name='size-chart-dashboard-create'),
    url(r'^dashboard/size-charts/(?P<pk>[0-9]+)/$',
        dashboard_views.size_chart_details,
        name='size-chart-dashboard-detail'),
    url(r'^dashboard/size-charts/(?P<pk>[0-9]+)/delete/$',
        dashboard_views.size_chart_delete,
        name='size-chart-dashboard-delete'),
]
