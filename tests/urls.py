from django.urls import path

from .views import DuckCreateView


urlpatterns = [
    path("", DuckCreateView.as_view()),
]
