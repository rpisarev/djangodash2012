from django.conf.urls import patterns, include, url

urlpatterns = patterns('core.views',
    # Examples:
    # url(r'^$', 'djangodash2012.views.home', name='home'),
    # url(r'^djangodash2012/', include('djangodash2012.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^$', 'main',name='core_main'),
    url(r'^(?P<obj_slug>[-\w]+)$', 'object',name='core_object'),
    url(r'^(?P<obj_slug>[-\w]+)/(?P<year>[0-9]+)$', 'object_year',name='core_object_year'),

    url(r'^$', 'test_google',),
    url(r'^$', 'test_instagram',),
    url(r'^$', 'test_flickr',),

)
