from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from user.models import UserProfile
from . import models

class UserPreferences(forms.ModelForm):
    class Meta():
        model = UserProfile
        fields = ('user', 'email')
        #user = forms.CharField(label='Your Name')
        #username = forms.CharField(label='Your Username', max_length=30)
        #email = forms.EmailField(label='email')
