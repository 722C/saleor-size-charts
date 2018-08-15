# saleor-size-charts

Size Chart Plugin for [Saleor](https://github.com/mirumee/saleor)

This provides a (currently skeleton) implementation of size charts. This is currently built for the `v2018.6` tag of Saleor.

Adding the size chart as a separate model allows for the size chart to be applied at multiple levels.

---

## Installation

To install, `pip install` the package as such:

```bash
pip install git+git://github.com/722c/saleor-size-charts.git#egg='saleor-size-charts'
```

Or list the package in your `requirements.txt` as such:

```
git+git://github.com/722c/saleor-size-charts.git#egg='saleor-size-charts'
```

Alternatively, this can be installed as a Git submodule directly in the root directory of your Saleor instance.

## Configuration

Once you have installed the app, you will need to add a few things to your project:

Add the app to your installed apps (the order doesn't matter):

```python
INSTALLED_APPS = [
    ...

    # Saleor plugins
    'saleor-size-charts.size_charts',

    ...
]
```

Add the apps URLs to your root `urls.py` in the `translatable_urlpatterns` near the bottom (this will allow any native Saleor URLs to be matched beforehand):

```python
translatable_urlpatterns = [
    ...
    url(r'^search/', include((search_urls, 'search'), namespace='search')),

    # URLs for saleor-size-charts
    url(r'', include('saleor-size-charts.size_charts.urls')),

    url(r'', include('payments.urls'))
]
```

Finally, add the link to the dashboard by importing the template tag in `templates/dashboard/base.html` and putting it where you want in the side nav:

```django
<!DOCTYPE html>
{% load staticfiles i18n %}
 ...

 <!-- This is template tag you will need to load. -->
{% load size_charts_side_nav from size_charts %}

...

<ul class="side-nav">
  <li class="nav-home">
    <a href="{% url 'dashboard:index' %}">
      {% trans "Home" context "Dashboard homepage" %}
    </a>
  </li>
  {% if perms.product.view_product or perms.product.view_category %}
  <li class="side-nav-section" id="first">
    ...
  </li>
  {% endif %}

  <!-- Add in the saleor-size-charts where you want. -->
  {% size_charts_side_nav %}

  ...
</ul>

...
```
