from django.conf.urls import url

from .views import IndexView, ContactView, LoginView, LogoutView, \
    RegisterView, AccountDetailsView, ChangePasswordView, SearchView, \
    SaveFeedbackView, MySightingView, NewSightingView, EditSightingView, \
    DeleteSightingView, AllSightingView, DetailSightingView

urlpatterns = [
    # ex: /motor/
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^contact/$', ContactView.as_view(), name='contact'),
    url(r'^account/$', AccountDetailsView.as_view(), name='account_details'),
    url(r'^register/$', RegisterView.as_view(), name="register"),
    url(r'^login/$', LoginView.as_view(), name="login"),
    url(r'^logout/$', LogoutView.as_view(), name="logout"),
    url(r'^change-password/$', ChangePasswordView, name="change_password"),
    url(r'^search/$', SearchView.as_view(), name='partsearch-search'),
    url(r'^feedback/$', SaveFeedbackView, name='save-feedback'),
    url(r'^all-sighting/$', AllSightingView.as_view(), name='all_sighting'),
    url(r'^sighting/(?P<id>\d+)/$', DetailSightingView.as_view(),
        name='detail_sighting'),
    url(r'^my-sighting/$', MySightingView.as_view(), name='my_sighting'),
    url(r'^new-sighting/$', NewSightingView.as_view(), name='new_sighting'),
    url(r'^edit-sighting/(?P<id>\d+)/$', EditSightingView.as_view(),
        name='edit_sighting'),
    url(r'^delete-sighting/(?P<id>\d+)/$', DeleteSightingView.as_view(),
        name='delete_sighting'),
]
