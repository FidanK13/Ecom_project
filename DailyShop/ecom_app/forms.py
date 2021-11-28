from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model

class RegisterForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'username', 'password1', 'password2')
        #labels = {'is_active': False}


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Email / Username')