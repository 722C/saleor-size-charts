from django import forms
from django.db.models import Q
from django.utils.translation import pgettext_lazy

from saleor.product.models import Category
from ..models import SizeChart


class SizeChartForm(forms.ModelForm):

    class Meta:
        model = SizeChart
        verbose_name_plural = 'size charts'
        exclude = []
