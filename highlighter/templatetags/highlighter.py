
from django import template

from .. import utils


register = template.Library()


@register.filter
def highlight(text, value):
    return utils.highlight(text, value)
