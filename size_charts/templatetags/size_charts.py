from django import template

register = template.Library()


@register.inclusion_tag('size_charts/dashboard/side_nav_inclusion.html',
                        takes_context=True)
def size_charts_side_nav(context):
    return context
