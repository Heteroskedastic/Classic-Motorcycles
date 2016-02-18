from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db.utils import IntegrityError
from django.shortcuts import render, HttpResponseRedirect

from django.views.generic import FormView


from .forms import RegisterForm, ChangeUserDetailsForm              

def RegisterView(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():                                   
            try:
                user = User.objects.create_user(
                    email=form.cleaned_data['email'],
                    username=form.cleaned_data['username'],
                    first_name=form.cleaned_data['first_name'],
                    last_name=form.cleaned_data['last_name'],
                    password=form.cleaned_data['password1'])
                return render(request, 'registration/register.html', {'success': True}) 
            except IntegrityError:
                form.add_error('username', 'Username already taken!')
    else:
        form = RegisterForm()
                
    return render(request, 'registration/register.html', {'form': form})

@login_required
def AccountView(request):
    if request.method == 'POST':
        form = ChangeUserDetailsForm(request.POST, instance=request.user)
        if form.is_valid():                                   
            form.save()
            return render(request, 'registration/account_details.html', 
                {'success': True,
                 'form': form})
    else:
        form = ChangeUserDetailsForm(instance=request.user)
    return render(request, 'registration/account_details.html', {'form': form})  