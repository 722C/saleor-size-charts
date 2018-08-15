from django.utils.translation import npgettext, pgettext_lazy
from django_filters import (CharFilter, OrderingFilter)

from saleor.core.filters import SortedFilterSet

from ..models import SizeChart

SORT_BY_FIELDS = {
    'name': pgettext_lazy('Size chart list sorting option', 'name')}


class SizeChartFilter(SortedFilterSet):
    name = CharFilter(
        label=pgettext_lazy('Size chart list filter label', 'Name'),
        lookup_expr='icontains')
    sort_by = OrderingFilter(
        label=pgettext_lazy('Size chart list filter label', 'Sort by'),
        fields=SORT_BY_FIELDS.keys(),
        field_labels=SORT_BY_FIELDS)

    class Meta:
        model = SizeChart
        fields = []

    def get_summary_message(self):
        counter = self.qs.count()
        return npgettext(
            'Number of matching records in the dashboard size charts list',
            'Found %(counter)d matching size chart',
            'Found %(counter)d matching size charts',
            number=counter) % {'counter': counter}
