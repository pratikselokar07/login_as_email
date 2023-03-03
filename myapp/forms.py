from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User

class CustomUser(UserCreationForm):
    class Meta:
        model =User
        fields=('email','phone_number')

class CustomAuthentication(AuthenticationForm):
    email=forms.CharField(label='Email Id :')
    password=forms.CharField(label='Password :', widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        del self.fields['username']

    class Meta:
        model=User
        field=('email','password')