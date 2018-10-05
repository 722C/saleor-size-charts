from django import forms
from django.db.models import Q
from django.utils.translation import pgettext_lazy

from saleor.product.models import Category, Product
from ..models import SizeChart

from django.urls import reverse_lazy
from saleor.dashboard.forms import AjaxSelect2MultipleChoiceField


class SizeChartForm(forms.ModelForm):
    products = AjaxSelect2MultipleChoiceField(
        queryset=Product.objects.all(),
        fetch_data_url=reverse_lazy('dashboard:ajax-products'), required=False)

    class Meta:
        model = SizeChart
        verbose_name_plural = 'size charts'
        exclude = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:
            self.fields['products'].set_initial(self.instance.products.all())
