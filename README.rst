Django HTML5 Colorfield
#######################

This module fills the need of having a 'colorfield' that's usable in both
django models and forms.

Usage
=====

::

    from colorfield import ColorField


    class MyModel(models.Model):
        color = ColorField()


Thanks
======

Many thanks to Jared Forsyth and others for the original javascript version of
this package.
