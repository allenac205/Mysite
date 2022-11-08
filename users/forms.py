
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms



class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={"class":"input input-bordered w-full max-w-xs", "placeholder":"Enter you email"}))
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={"class":"input input-bordered w-full max-w-xs", "placeholder":"Enter your name"}))
    password1 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={"class":"input input-bordered w-full max-w-xs", "placeholder":"Type here"}))
    password2 = forms.CharField(required=True, widget=forms.TextInput(attrs={"class":"input input-bordered w-full max-w-xs", "placeholder":"Type here"}))

    class Meta:
        model = User
        fields = ('email', 'username', 'password1', 'password2')