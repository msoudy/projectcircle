from django.conf.urls.defaults import patterns, include, url
from django.conf import settings

from django.views.generic.simple import direct_to_template

import os
APP_PATH = os.path.abspath(os.path.dirname(__file__))

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ahmadsweb.views.home', name='home'),
    (r'^$', 'circleight.views.index'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)


urlpatterns += patterns('',
    (r'^css/(?P<path>.*)$', 'django.views.static.serve',
                         {'document_root': os.path.join(APP_PATH, 'static/css'), 'show_indexes': settings.DEBUG}),
    (r'^js/(?P<path>.*)$', 'django.views.static.serve',
                         {'document_root': os.path.join(APP_PATH, 'static/js'), 'show_indexes': settings.DEBUG}),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve',
                         {'document_root': os.path.join(APP_PATH, 'static/media'), 'show_indexes': settings.DEBUG}),
)