import re

from django.db import models
from django.core.validators import RegexValidator
from django.forms import TextInput
from django.utils.translation import ugettext_lazy as _


color_re = re.compile('^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$')
validate_color = RegexValidator(color_re, _(u'Enter a valid hex color (without the leading #).'), 'invalid')


class ColorInput(TextInput):
    input_type = 'color'


class ColorField(models.CharField):
    default_validators = [validate_color]

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 10
        super(ColorField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        kwargs['widget'] = ColorInput
        return super(ColorField, self).formfield(**kwargs)

try:
    from south.modelsinspector import add_introspection_rules
    add_introspection_rules([], ['^colorfield\.fields\.ColorField'])
except ImportError:
    pass
