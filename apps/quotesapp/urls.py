from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^quotes$', views.quotes),
    url(r'^login$', views.login),
    url(r'^addquote$', views.addquote),
    url(r'^', views.undefined)
]
