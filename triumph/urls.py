from django.conf.urls import patterns, include, url

from .views import SearchView

urlpatterns = patterns('',
                       url(r'^$', SearchView.as_view(), name='triumph-search'),
                       )
