from django.conf.urls import patterns, include, url
import sys
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djangodash2012.views.home', name='home'),
    # url(r'^djangodash2012/', include('djangodash2012.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^', include('core.urls')),


)

RUNNING_DEVSERVER = (sys.argv[1] == 'runserver')
if RUNNING_DEVSERVER:
    urlpatterns+=patterns('',url(r'^', include('local.urls')),)