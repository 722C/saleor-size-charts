from django.db import models

from django.utils.translation import pgettext_lazy

from versatileimagefield.fields import VersatileImageField

from saleor.core.permissions import MODELS_PERMISSIONS


# Add in the permissions specific to our models.
MODELS_PERMISSIONS += [
    'size_charts.view',
    'size_charts.edit'
]


class SizeChart(models.Model):
    name = models.CharField(max_length=255)
    chart = VersatileImageField(upload_to='size-charts')
    product_type = models.ManyToManyField(
        'product.ProductType', related_name='size_chart',
        blank=True)
    category = models.ManyToManyField(
        'product.Category', related_name='size_chart',
        blank=True)
    products = models.ManyToManyField(
        'product.Product', related_name='size_chart',
        blank=True)
    added = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = 'size_charts'

        permissions = (
            ('view', pgettext_lazy('Permission description',
                                   'Can view size charts')
             ),
            ('edit', pgettext_lazy('Permission description',
                                   'Can edit size charts')))

    def __str__(self):
        return self.name
