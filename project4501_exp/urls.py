from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^home/$',views.home),
    #url(r'^home/(?P<class_id>[0-9]+)/(?P<info_id>[0-9]+)/$', views.home),

    url(r'^product/$',views.product),
    #url(r'^product/(?P<class_id>[0-9]+)/(?P<info_id>[0-9]+)/$', views.product),

#    url(r'^admin/', include(admin.site.urls)),
)


#product page
#course and course info 

#homepage. 
#course and course info.  

#
#
#
#
