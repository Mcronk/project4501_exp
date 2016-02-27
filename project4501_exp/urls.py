from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^homepageCourse/$',views.homeCourse),
    url(r'^homepageCourse/(?P<class_id>[0-9]+)/(?P<info_id>[0-9]+)/$', views.homeCourse),

    url(r'^product/$',views.productCourse),
    url(r'^productPageCourse/(?P<class_id>[0-9]+)/(?P<info_id>[0-9]+)/$', views.productCourse),

    url(r'^admin/', include(admin.site.urls)),
)


#product page
#course and course info 

#homepage. 
#course and course info.  

#
#
#
#
