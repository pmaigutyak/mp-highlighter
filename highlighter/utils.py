
import re

from django.utils.safestring import mark_safe


def highlight(text, value, tag_name='span', tag_class='highlighted'):

    if not text or not value:
        return ''

    pattern = re.compile(r'(%s)' % re.escape(value), re.IGNORECASE)

    replace_to = r'<{tag_name} class="{tag_class}">\1</{tag_name}>'.format(
        tag_name=tag_name, tag_class=tag_class)

    return mark_safe(pattern.sub(replace_to, text))
