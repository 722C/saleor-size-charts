from django import template

register = template.Library()


@register.inclusion_tag('size_charts/dashboard/side_nav_inclusion.html',
                        takes_context=True)
def size_charts_side_nav(context):
    return context


@register.inclusion_tag('size_charts/image.html')
def size_chart(product):
    size_chart = (product.size_chart.first() or
                  product.category.size_chart.first() or
                  product.product_type.size_chart.first())

    return {
        'size_chart': size_chart
    }
