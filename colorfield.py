import re

from django.core.validators import RegexValidator
from django.db import models
from django.forms import TextInput
from django.utils.translation import gettext_lazy as _


color_re = re.compile(r"^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$")
validate_color = RegexValidator(
    color_re, _("This must be a valid hex color."), "invalid"
)


class ColorInput(TextInput):
    input_type = "color"


class ColorField(models.CharField):
    default_validators = [validate_color]

    def __init__(self, *args, **kwargs):
        kwargs["max_length"] = 7
        super().__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        kwargs["widget"] = ColorInput
        return super().formfield(**kwargs)
