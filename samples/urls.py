from django.conf.urls import url, include
from .views import newsample, labdetails

urlpatterns = [
    url(r'^newsample', newsample, name='newsample'),
    url(r'^labdetails', labdetails, name='labdetails'),
]