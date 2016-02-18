from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.Form):
    email = forms.EmailField()
    username = forms.CharField(label='User Name', max_length=50)
    first_name = forms.CharField(label='First Name', max_length=50)
    last_name = forms.CharField(label='Last Name', max_length=50)
    password1 = forms.CharField(label='Password', max_length=50, widget=forms.PasswordInput())
    password2 = forms.CharField(label='Confirm Password', max_length=50, widget=forms.PasswordInput())
    
    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 != password2:
            # Make sure the passwords match.
            msg = "Passwords don't match!"
            self.add_error('password1', msg)
            self.add_error('password2', msg)
            
class ChangeUserDetailsForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']