from django.conf.urls import patterns, include, url

from .views import SearchView, SaveFeedback

urlpatterns = patterns('',
                       url(r'^$', SearchView.as_view(), name='partsearch-search'),
                       url(r'^feedback$', SaveFeedback, name='save-feedback'),
                       )
