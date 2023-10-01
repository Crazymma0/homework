from django import forms


class RegisterForm(forms.Form):
    username = forms.CharField(min_length=3, max_length=32)
    password1 = forms.CharField(min_length=8, widget=forms.PasswordInput())
    password2 = forms.CharField(min_length=8, widget=forms.PasswordInput())


class LoginForm(forms.Form):
    username = forms.CharField(min_length=3, max_length=32)
    password = forms.CharField(min_length=8, widget=forms.PasswordInput())


