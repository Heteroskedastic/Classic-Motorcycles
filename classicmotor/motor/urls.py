from django.conf.urls import url

from .views import IndexView, HomeView, ContactView, LoginView, LogoutView, \
    RegisterView, AccountDetailsView, ChangePasswordView, SearchView, \
    SaveFeedbackView

urlpatterns = [
    # ex: /motor/
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^home/$', HomeView.as_view(), name='home'),
    url(r'^contact/$', ContactView.as_view(), name='contact'),
    url(r'^account/$', AccountDetailsView.as_view(), name='account_details'),
    url(r'^register/$', RegisterView.as_view(), name="register"),
    url(r'^login/$', LoginView.as_view(), name="login"),
    url(r'^logout/$', LogoutView.as_view(), name="logout"),
    url(r'^change-password/$', ChangePasswordView, name="change_password"),
    url(r'^search/$', SearchView.as_view(), name='partsearch-search'),
    url(r'^feedback/$', SaveFeedbackView, name='save-feedback'),
]
