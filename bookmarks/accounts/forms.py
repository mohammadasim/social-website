from django import forms


class LoginForm(forms.Form):
    """
    Form to login users
    """
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
