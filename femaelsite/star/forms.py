from django import forms
from .models import Category

class AddPostForm(forms.Form):

    title = forms.CharField(max_length = 255, label = "Заголовок")
    slug = forms.SlugField(max_length = 255, label = "URL")
    game = forms.CharField(max_length = 255, label = "Игра")
    ingredients = forms.JSONField(initial = list, label = "Ингредиетны")
    effect = forms.CharField(max_length = 255, label = "Эффект")
    preparation = forms.CharField(widget = forms.Textarea(), label = "Способ приготовления")

    cat = forms.ModelChoiceField(queryset = Category.objects.all(), empty_label = "Не выбрано" ,label = "Категория")