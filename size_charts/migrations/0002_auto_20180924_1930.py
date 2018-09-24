# Generated by Django 2.0.3 on 2018-09-24 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('size_charts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sizechart',
            name='category',
            field=models.ManyToManyField(blank=True, related_name='size_chart', to='product.Category'),
        ),
        migrations.AlterField(
            model_name='sizechart',
            name='product_type',
            field=models.ManyToManyField(blank=True, related_name='size_chart', to='product.ProductType'),
        ),
        migrations.AlterField(
            model_name='sizechart',
            name='products',
            field=models.ManyToManyField(blank=True, related_name='size_chart', to='product.Product'),
        ),
    ]
