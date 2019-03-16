from django.conf.urls import include, url
from accounts.views import logout, login, register
from accounts import url_reset


urlpatterns = [
    url(r'^logout/$', logout, name="logout"),
    url(r'^login/$', login, name="login"),
    url(r'^register/$', register, name="register"),
    url(r'^password-reset/', include(url_reset))
]