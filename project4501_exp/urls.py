from django.conf.urls import patterns, include, url
from django.contrib import admin
from . import views

urlpatterns = patterns('',
    url(r'^v1/create_account/(?P<username>)/(?P<password>)/$',views.create_account),
    url(r'^v1/login/$', views.login),
    url(r'^v1/logout/(?P<token>)/$',views.logout),
    url(r'^v1/create_listing/(?P<token>)/(?P<listing>)/$',views.create_listing),

    url(r'^v1/courses/$',views.courses),
    url(r'^v1/course/$',views.course),
    url(r'^v1/course/(?P<course_pk>[0-9]+)/$', views.course),


)

#createAuth
#checkAuth

