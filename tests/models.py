from django.db import models

from colorfield import ColorField


class Duck(models.Model):
    color = ColorField()
