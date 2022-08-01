from django import forms
from .models import *


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class C(forms.ModelForm):
    class Meta:
        model = Comment_pig
        fields = ['comment']


class C1(forms.ModelForm):
    class Meta:
        model = Comment_kenguru
        fields = ['comment']
