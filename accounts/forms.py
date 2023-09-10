from django import forms
from django.forms import ModelForm
from .models import Detail

class SignUpForm(forms.Form):
    username = forms.CharField(max_length=150)
    first_name = forms.CharField(max_length=150)
    last_name = forms.CharField(max_length=150)
    password = forms.CharField(
        max_length=150,
        widget=forms.PasswordInput,
    )
    password_confirmation = forms.CharField(
        max_length=150,
        widget=forms.PasswordInput,
    )


class UserEditForm(forms.Form):
    username = forms.CharField(max_length=150)
    first_name = forms.CharField(max_length=150)
    last_name = forms.CharField(max_length=150)


class PasswordUpdateForm(forms.Form):
    current_password = forms.CharField(
        max_length=150,
        widget=forms.PasswordInput,
    )
    new_password = forms.CharField(
        max_length=150,
        widget=forms.PasswordInput,
    )
    password_confirmation = forms.CharField(
        max_length=150,
        widget=forms.PasswordInput,
    )


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(
        max_length=150,
        widget=forms.PasswordInput,
    )


class DetailForm(ModelForm):
    class Meta:
        model = Detail
        fields = (
            'avatar',
            'species',
            'description',
            'gender'
        )
