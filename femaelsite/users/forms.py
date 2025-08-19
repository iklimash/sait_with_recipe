from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django import forms

class LoginUserForm(forms.Form):
    username = forms.CharField(
        label='Имя пользователя',
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'id': 'username',
            'placeholder': 'Введите имя пользователя'
        }),
        required=True
    )
    
    password = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(attrs={
            'class': 'form-input',
            'id': 'password',
            'placeholder': 'Введите ваш пароль'
        }),
        required=True
    )

class RegisterUserForm(UserCreationForm):
    username = forms.CharField(
        label='Имя пользователя',
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'id': 'username',
            'placeholder': 'Введите имя пользователя'
        }),
        required=True
    )
    password1 = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(attrs={
            'class': 'form-input',
            'id': 'password1',
            'placeholder': 'Введите ваш пароль'
        }),
        required=True
    )
    password2 = forms.CharField(
        label='Подтверждение пароля',
        widget=forms.PasswordInput(attrs={
            'class': 'form-input',
            'id': 'password2',
            'placeholder': 'Повторите ваш пароль'
        }),
        required=True
    )
    class Meta:
        model = get_user_model()
        fields = ['username', 'password1', 'password2']

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError('Пароли не совпадают!')
        return cd['password']