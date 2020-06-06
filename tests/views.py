from django.views.generic import CreateView

from .models import Duck


class DuckCreateView(CreateView):
    model = Duck
    fields = ["color"]
