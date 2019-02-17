from django.conf.urls import url, include
from .views import newsample

urlpatterns = [
    url(r'^newsample', newsample, name='newsample'),
]