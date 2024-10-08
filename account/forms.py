from django import forms
from .models import Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


class RegisterUser(UserCreationForm):

    class Meta():
        model = get_user_model()
        fields = ['username','first_name','last_name','email', 'password1', 'password2']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude =('user',)


