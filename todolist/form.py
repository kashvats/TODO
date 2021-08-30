from django.contrib.auth.models import User
from django import forms
from .models import todo
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages




class regi(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']


class todotask(forms.ModelForm):
    class Meta:
        model = todo
        fields = ['Task']