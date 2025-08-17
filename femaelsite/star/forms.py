from django import forms
from .models import Category

class AddPostForm(forms.Form):

    title = forms.CharField(widget = forms.Textarea(attrs = {'cols': 60, 'rows': 1}), label = "Заголовок", required = True,
                             error_messages = {
                                'required': 'Без заголовка никак ;('
                            })
    slug = forms.SlugField(widget = forms.Textarea(attrs = {'cols': 60, 'rows': 1}), label = "URL")
    game = forms.CharField(widget = forms.Textarea(attrs = {'cols': 60, 'rows': 1}), label = "Игра")
    ingredients = forms.JSONField(initial = list, widget=forms.Textarea(attrs={'cols': 60, 'rows': 5}), label = "Ингредиетны")
    effect = forms.CharField(widget = forms.Textarea(attrs = {'cols': 60, 'rows': 1}), label = "Эффект")
    preparation = forms.CharField(widget = forms.Textarea(attrs = {'cols': 60, 'rows': 5}), label = "Способ приготовления")

    cat = forms.ModelChoiceField(queryset = Category.objects.all(), empty_label = "Не выбрана" ,label = "Категория")