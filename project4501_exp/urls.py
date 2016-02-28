from django.conf.urls import patterns, include, url
from django.contrib import admin
from . import views

urlpatterns = patterns('',

    url(r'^home/$',views.home),

    url(r'^product/$',views.product),
    url(r'^product/(?P<course_pk>[0-9]+)/$', views.product),

)


