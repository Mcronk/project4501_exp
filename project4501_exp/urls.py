from django.conf.urls import patterns, include, url
from django.contrib import admin
from . import views

urlpatterns = patterns('',
    url(r'^v1/createAuth/(?P<username>)/(?P<password>)/$',views.createAuth),
    url(r'^v1/checkAuth/(?P<token>)/$',views.checkAuth),
    url(r'^v1/courses/$',views.courses),
    url(r'^v1/course/$',views.course),
    url(r'^v1/course/(?P<course_pk>[0-9]+)/$', views.course),


)

#createAuth
#checkAuth

