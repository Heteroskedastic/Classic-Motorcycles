from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
from django import forms

from .models import Sighting


class RegistrationForm(forms.ModelForm):
    """
    new user register
    """
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    password1 = forms.CharField(widget=forms.PasswordInput,
                                required=True,
                                label="Confirm password ")

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password',
                  'password1']

    def clean_password1(self):
        try:
            password1 = self.cleaned_data["password"]
            password2 = self.cleaned_data["password1"]
            if password1 == '' or password2 == '':
                raise forms.ValidationError("You must enter password")
            if password1 and password2 and password1 != password2:
                raise forms.ValidationError("Passwords don't match")
            return self.cleaned_data
        except:
            raise forms.ValidationError(
                ("Password doesn't match."))


class AccountDetailsForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']


class SightingForm(forms.ModelForm):
    class Meta:
        model = Sighting
        fields = ['make', 'model', 'year', 'frame_number', 'engine_number',
                  'notes', 'country', 'state', 'city', 'contact', ]

    def __init__(self, *args, **kwargs):
        super(SightingForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            field_label = self.fields[field].label
            if self.fields[field].required and field_label:
                self.fields[field].widget.attrs.update({
                    'placeholder': field_label,
                })
                self.fields[field].label = mark_safe(
                    field_label + ' <span class="text text-danger">*</span>')


class NewSightingForm(SightingForm):
    pass


class EditSightingForm(SightingForm):
    pass
