from django import forms
from .models import Category

class AddPostForm(forms.Form):

    title = forms.CharField(max_length = 255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    slug = forms.SlugField(max_length = 255)
    game = forms.CharField(max_length = 255)
    ingredients = forms.JSONField(initial = list)
    effect = forms.CharField(max_length = 255)
    preparation = forms.CharField(widget = forms.Textarea())

    cat = forms.ModelChoiceField(queryset = Category.objects.all())