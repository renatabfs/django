from django.views.generic import TemplateView
from .views import IndexView

urlpatterns = [
    path ('inicio/', IndexView.as_view (), name = 'inicio')
]