from django.conf.urls import patterns, include, url
from django.contrib import admin
from . import views

urlpatterns = patterns('',
    url(r'^courses/$',views.courses),
    url(r'^course/$',views.course),
    url(r'^course/(?P<course_pk>[0-9]+)/$', views.course),
)

