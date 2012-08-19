from django.conf.urls import patterns, include, url

urlpatterns = patterns('local.views',
    # Examples:
    # url(r'^$', 'djangodash2012.views.home', name='home'),
    # url(r'^djangodash2012/', include('djangodash2012.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^parse$', 'parse'),
    url(r'^clean', 'clean_images'),
)
