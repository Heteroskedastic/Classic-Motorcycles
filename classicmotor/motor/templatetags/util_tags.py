from django import template
from django.apps import apps
from urllib.parse import urlencode
from collections import OrderedDict
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag(takes_context=True)
def active_if(context, *view_names):
    if context.request.resolver_match.view_name in view_names:
        return 'active'
    return ''


@register.filter(name='addcss')
def addcss(field, css):
    return field.as_widget(attrs={"class": css})


@register.filter
def join_and(value):
    """Given a list of strings, format them with commas and spaces, but
    with 'and' at the end.

    >>> join_and(['apples', 'oranges', 'pears'])
    "apples, oranges, and pears"

    """
    # convert numbers to strings
    value = [str(item) for item in value]
    if len(value) == 0:
        return ''
    if len(value) == 1:
        return value[0]

    # join all but the last element
    all_but_last = ", ".join(value[:-1])
    return "%s, and %s" % (all_but_last, value[-1])


@register.simple_tag(takes_context=True)
def sorting_link(context, text, value, field='order_by', direction=''):
    dict_ = context.request.GET.copy()
    icon = 'fa fa-fw '
    link_css = ''
    if field in dict_.keys():
        if dict_[field].startswith('-') and dict_[field].lstrip('-') == value:
            dict_[field] = value
            icon += 'fa-sort-desc'
            link_css += 'text-italic'
        elif dict_[field].lstrip('-') == value:
            dict_[field] = "-" + value
            icon += 'fa-sort-asc'
            link_css += 'text-italic'
        else:
            dict_[field] = direction + value
            icon += 'fa-sort gray2-color'
    else:
        dict_[field] = direction + value
        icon += 'fa-sort gray2-color'
    url = urlencode(OrderedDict(sorted(dict(dict_).items())), True)

    return mark_safe('<a href="?{0}" class="{1}">{2}<i class="{3}">'
                     '</i></a>'.format(url, link_css, text, icon))


def _get_field(Model, field_name):
    if isinstance(Model, str):
        Model = apps.get_model(Model)

    return Model._meta.get_field(field_name)


@register.simple_tag
def get_verbose_field_name(Model, field_name):
    """
    Returns verbose_name for a field.
    """
    field = _get_field(Model, field_name)
    return field.verbose_name


@register.simple_tag(takes_context=True)
def page_size_combo(context, *sizes, **kwargs):
    if not sizes:
        sizes = (10, 20, 30, 50)
    page_size = context.request.GET.get('page_size') or None
    html = 'Page Size <select class="page-size" name="page_size">'
    for size in sizes:
        selected = ('selected' if str(size) == str(page_size) else '')
        html += '<option value="{0}" {1}>{0}</option>'.format(
            size, selected)
    html += '</select>'
    return mark_safe(html)
