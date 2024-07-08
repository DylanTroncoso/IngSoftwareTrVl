from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'Email', 'id': 'email', 'style': 'margin-bottom: -100px;'})
    )
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Usuario', 'id': 'username ', 'style': 'margin-bottom: -100px'})
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña', 'id': 'password1', 'style': 'margin-bottom: -100px'})
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirmar contraseña', 'id': 'password2', 'style': 'margin-bottom: -100px'})
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Usuario', 'style': 'margin-bottom: -100px;'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña'})
    )