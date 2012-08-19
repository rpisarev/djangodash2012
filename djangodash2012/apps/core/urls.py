from django.conf.urls import patterns, include, url

urlpatterns = patterns('core.views',
    # Examples:
    # url(r'^$', 'djangodash2012.views.home', name='home'),
    # url(r'^djangodash2012/', include('djangodash2012.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^$', 'main', name='core_main'),
    url(r'^vote/(?P<image_id>[0-9]+)/(?P<value>(up|down))$', 'vote', name='core_vote'),

    url(r'^random/$', 'random', name='core_random'),
    url(r'^about/$', 'about', name='core_about'),
    url(r'^rating/$', 'rating', name='core_rating'),

    url(r'^m/(?P<miracle_slug>[-\w]+)/$', 'miracle', name='core_miracle'),
    url(r'^m/(?P<miracle_slug>[-\w]+)/(?P<year>[0-9]+)$', 'miracle_year', name='core_miracle_year'),
)
