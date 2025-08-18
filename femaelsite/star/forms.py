from django import forms
from .models import Category, recipe


class AddPostForm(forms.ModelForm):
    class Meta:
        model = recipe
        fields = ['title', 'slug', 'game', 'ingredients', 'effect', 'preparation', 'cat']
        
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название рецепта'
            }),
            'slug': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Уникальный идентификатор (латинские буквы, цифры, дефисы)'
            }),
            'game': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название игры'
            }),
            'ingredients': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Каждый ингредиент с новой строки'
            }),
            'effect': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 2,
                'placeholder': 'Эффект от рецепта'
            }),
            'preparation': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Подробное описание приготовления'
            }),
            'cat': forms.Select(attrs={
                'class': 'form-control'
            })
        }