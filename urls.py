from django.conf.urls.defaults import *
urlpatterns = patterns('',
    (r'^update_xml/',  'main.views.update_xml'),
    (r'^newEPG/regions/(?P<area>\d+)/$',  'main.views.regions'),
    (r'^regions/(?P<area>\d+)/$',  'main.views.regions'),
    (r'^generate/$',  'main.views.generate'),
    (r'^newEPG/generate/$',  'main.views.generate'),
    (r'^channels/(?P<region>\d+)/$',  'main.views.channels'),
    (r'^newEPG/channels/(?P<region>\d+)/$',  'main.views.channels'),
    (r'^/$',  'main.views.index'),
    (r'^$',  'main.views.index'),
)
