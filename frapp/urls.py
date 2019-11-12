from django.conf.urls import url
from .views import frapp

urlpatterns = [
    url(r'', frapp, name='frapp'),
]
