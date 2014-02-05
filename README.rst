Django HTML5 Colorfield
#######################

This module fills the need of having a 'colorfield' that's usable in both
django models and forms. Requires django 1.7+.


Usage
=====

::

    from colorfield.fields import ColorField
    

    class MyModel(models.Model):
        color = ColorField()


Thanks
======

Many thanks to Jared Forsyth and others for the original javascript version of
this package.