from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe

import logging

logger = logging.getLogger(__name__)

register = template.Library()


@register.filter(is_safe=True)
@stringfilter
def custom_markdown(content):
    from SimpleBlog.utils import CommonMarkdown
    return mark_safe(CommonMarkdown.get_markdown(content))