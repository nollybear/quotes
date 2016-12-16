from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^quotes$', views.quotes),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
    url(r'^addquote$', views.addquote),
    url(r'^addfavorite/(?P<id>\d+)$', views.addfavorite),
    url(r'^user/(?P<id>\d+)$', views.user),
    url(r'^', views.undefined)
]
