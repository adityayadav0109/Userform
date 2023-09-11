from dataclasses import field
from django import forms
from django.forms import ModelForm

from .models import User

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'



class LoginForm(forms.Form):
    email =  forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
