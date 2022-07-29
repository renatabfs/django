from importlib.resources import path
from unicodedata import name
from django.urls import Path
from .views import IndexView


urlpatterns = [
    path('inicio/', IndexView.as_view(), name='inicio'),
]
