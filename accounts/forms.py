from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from accounts.models import User

class RegisterForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input-box', 'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input-box', 'placeholder': 'Confirm Password'}))
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'input-box', 'placeholder': 'Username'}),
            'email': forms.EmailInput(attrs={'class': 'input-box', 'placeholder': 'E-mail'}),
            'first_name': forms.TextInput(attrs={'class': 'input-box', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'input-box', 'placeholder': 'Last Name'}),
            'password1': forms.PasswordInput(attrs={'class': 'input-box', 'placeholder': 'Password'}),
            'password2': forms.PasswordInput(attrs={'class': 'input-box', 'placeholder': 'Confirm Password'}),
        }

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-box', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input-box', 'placeholder': 'Password'}))
    class Meta:
        model = User
        fields = ['username', 'password']  