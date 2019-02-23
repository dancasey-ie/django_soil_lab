from django.conf.urls import url, include
from .views import newsample, labdetails, viewreport, receive, results

urlpatterns = [
    url(r'^newsample', newsample, name='newsample'),
    url(r'^labdetails', labdetails, name='labdetails'),
    url(r'^viewreport/(?P<sample_id>\d+)/$', viewreport, name="viewreport"),
    url(r'^receive/', receive, name="receive"),
    url(r'^results/', results, name="results")
]