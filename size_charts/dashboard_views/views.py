from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from django.shortcuts import get_object_or_404, redirect
from django.template.response import TemplateResponse
from django.utils.translation import pgettext_lazy

from saleor.core.utils import get_paginator_items
from saleor.dashboard.views import staff_member_required
from .filters import SizeChartFilter
from .forms import SizeChartForm

from ..models import SizeChart


@staff_member_required
@permission_required('size_charts.view')
def size_chart_list(request):
    size_charts = (
        SizeChart.objects.all().order_by('name'))
    size_chart_filter = SizeChartFilter(
        request.GET, queryset=size_charts)
    size_charts = get_paginator_items(
        size_charts, settings.DASHBOARD_PAGINATE_BY, request.GET.get('page'))
    # Call this so that cleaned_data exists on the filter_set
    size_chart_filter.form.is_valid()
    ctx = {
        'size_charts': size_charts, 'filter_set': size_chart_filter,
        'is_empty': not size_chart_filter.queryset.exists()}
    return TemplateResponse(request, 'size_charts/dashboard/list.html', ctx)


@staff_member_required
@permission_required('size_charts.edit')
def size_chart_create(request):
    size_chart = SizeChart()
    form = SizeChartForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        msg = pgettext_lazy('Dashboard message', 'Created size chart')
        messages.success(request, msg)
        return redirect('size-chart-dashboard-list')
    ctx = {'size_chart': size_chart, 'form': form}
    return TemplateResponse(request, 'size_charts/dashboard/detail.html', ctx)


@staff_member_required
@permission_required('size_charts.edit')
def size_chart_details(request, pk):
    size_chart = SizeChart.objects.get(pk=pk)
    form = SizeChartForm(
        request.POST or None, request.FILES or None, instance=size_chart)
    if form.is_valid():
        form.save()
        msg = pgettext_lazy(
            'Dashboard message', 'Updated size chart %s') % size_chart.name
        messages.success(request, msg)
        return redirect('size-chart-dashboard-list')
    ctx = {'size_chart': size_chart, 'form': form}
    return TemplateResponse(request, 'size_charts/dashboard/detail.html', ctx)


@staff_member_required
@permission_required('size_charts.edit')
def size_chart_delete(request, pk):
    size_chart = get_object_or_404(SizeChart, pk=pk)
    if request.method == 'POST':
        size_chart.delete()
        msg = pgettext_lazy('Dashboard message',
                            'Removed size chart %s') % size_chart
        messages.success(request, msg)
        return redirect('size-chart-dashboard-list')
    return TemplateResponse(
        request, 'size_charts/dashboard/modal/confirm_delete.html', {'size_chart': size_chart})
