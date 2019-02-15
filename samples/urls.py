from django.conf.urls import url, include
from .views import newsample, submitsample

urlpatterns = [
    url(r'^newsample', newsample, name='newsample'),
    url(r'^submitsample', submitsample, name='submitsample'),
]