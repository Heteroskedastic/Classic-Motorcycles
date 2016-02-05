from django.conf.urls import patterns, include, url

from home.views import *

urlpatterns = patterns('',
                       url(r'^$', HomeView.as_view(), name='home'),
                       url(r'^online_store/$', OnlineStoreView.as_view(),
                           name='online_store'),
                       url(r'^blog/$', BlogView.as_view(),
                           name='blog'),
                       url(r'^daves_corner/$', DavesCornerView.as_view(),
                           name='daves_corner'),
                       url(r'^contact_us/$', ContactUsView.as_view(),
                           name='contact_us'),
                       )
