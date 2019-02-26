from django.conf.urls import url, include
from .views import viewreport, receive, results, submit

urlpatterns = [
    url(r'^viewreport/(?P<sample_id>\d+)/$', viewreport, name="viewreport"),
    url(r'^receive/', receive, name="receive"),
    url(r'^results/', results, name="results"),
    url(r'^submit/(?P<status_id>\d+)/$', submit, name="submit")
]