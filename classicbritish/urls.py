from django.conf.urls import patterns, include, url
from django.contrib import admin

from .views import RegisterView, AccountView

urlpatterns = patterns('',

	url(r'^', include('home.urls')),
	url(r'^search/', include('partsearch.urls')),

    # url(r'^blog/', include('blog.urls')),
    #User Management
    
    url(r'^register$', RegisterView, name='register_view'),
    url(r'^account_details/', AccountView, name='account_details'),
    #Django's default handlers for login, logout, password reset and change
    #url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^accounts/', include('allauth.urls')),
    
    #Admin
    url(r'^admin/', include(admin.site.urls)),
)
