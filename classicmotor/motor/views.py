from django.conf import settings
from django.views.generic import View
from django.contrib.auth.views import password_change
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin

from classicmotor.helpers.utils import success_message, \
    send_form_errors
from .forms import RegistrationForm, AccountDetailsForm


class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "motor/index.html", {})


class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "motor/home.html", {})


class ContactView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "motor/contact.html", {})


class RegisterView(View):

    def get(self, request, *args, **kwargs):
        form = RegistrationForm()
        ctx = {"form": form}
        return render(request, "registration/register.html", ctx)

    def post(self, request, *args, **kwargs):
        form = RegistrationForm(request.POST)
        password = request.POST.get('password')
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(password)
            user.save()
            success_message('User registered successfully.', request)
            return redirect(self.get_success_url())
        else:
            send_form_errors(form, request)
        ctx = {"form": form}
        return render(request, "registration/register.html", ctx)

    def get_success_url(self):
        url = reverse('home')
        return url


class LoginView(View):

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return redirect(settings.LOGIN_REDIRECT_URL)
        form = AuthenticationForm()
        ctx = {"form": form}
        return render(request, "motor/login.html", ctx)

    def post(self, request, *args, **kwargs):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            next = request.GET.get('next') or settings.LOGIN_REDIRECT_URL
            return redirect(next)
        else:
            send_form_errors(form, request)
        ctx = {"form": form}
        return render(request, "motor/login.html", ctx)


class LogoutView(View):

    def get(self, request, *args, **kwargs):
        auth_logout(request)
        return redirect(reverse('login'))


class AccountDetailsView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        form = AccountDetailsForm(instance=request.user)
        return render(request, "motor/account_details.html", {'form': form})

    def post(self, request, *args, **kwargs):
        form = AccountDetailsForm(data=request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            success_message('Account Details saved successfully.', request)
        else:
            send_form_errors(form, request)
        ctx = {"form": form}
        return render(request, "motor/account_details.html", ctx)


def ChangePasswordView(request):
    redirect_url = reverse('account_details')
    response = password_change(
        request, template_name='motor/change_password.html',
        post_change_redirect=redirect_url)
    if request.method == 'POST' and response.status_code == 302 and \
            response.url == redirect_url:

        success_message('Password changed successfully.', request)

    return response

