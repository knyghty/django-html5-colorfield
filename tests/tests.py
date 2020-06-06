from django import forms
from django.test import TestCase

from .models import Duck


class DuckForm(forms.ModelForm):
    class Meta:
        model = Duck
        fields = ["color"]


class ColorFieldTestCase(TestCase):
    def test_colorfield_renders_with_html5_attribute(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'type="color"')

    def test_colorfield_validation(self):
        # Anything too long will fail in Django's validation.
        form = DuckForm(data={"color": "rebeccapurple"})
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors["color"],
            ["Ensure this value has at most 7 characters (it has 13)."],
        )

        # Color names aren't supported:
        # https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/color
        form = DuckForm(data={"color": "yellow"})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors["color"], ["This must be a valid hex color."])

        # Alpha channels are also not supported.
        form = DuckForm(data={"color": "#ffffffff"})
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors["color"],
            ["Ensure this value has at most 7 characters (it has 9)."],
        )

        # Short form.
        form = DuckForm(data={"color": "#fff"})
        self.assertTrue(form.is_valid())

        # Long form.
        form = DuckForm(data={"color": "#9b59d0"})
        self.assertTrue(form.is_valid())
