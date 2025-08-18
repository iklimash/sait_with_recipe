
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

# class LoginUserForm(forms.Form):

#     username = forms.CharField(label = 'login', widget = forms.TextInput(attrs = {'class': 'form-input'})) 
#     password = forms.CharField(label = 'login', widget = forms.PasswordInput(attrs = {'class': 'form-input'})) 
#     pass