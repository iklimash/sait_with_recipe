from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.template.loader import render_to_string

from .models import recipe


def index(request):
    
    data_index = { 'title': 'Главная страница'}
    return render(request, 'star/index.html', data_index)

def about(request):
    return render(request, 'star/about.html', { 'title': 'О нас'})

def show_recipe(request, recipe_id):
    recipe_obj  = get_object_or_404(recipe, pk = recipe_id)

    recipe_data ={
        'id': recipe_obj .id,
            'title': recipe_obj .title,
            'game': recipe_obj .game,
            'ingredients': recipe_obj .ingredients,  
            'effect': recipe_obj .effect,
            'preparation': recipe_obj.preparation
    }
            
    return render(request, 'star/recipe.html', {'recipe': recipe_data})

def catalog(request):

    recipes_queryset = recipe.objects.all()
    
    recipes_data = [
        {
            'id': recipe.id,
            'title': recipe.title,
            'game': recipe.game,
            'ingredients': recipe.ingredients,  
            'effect': recipe.effect,
            'preparation': recipe.preparation
        }
        for recipe in recipes_queryset
    ]
    return render(request, 'star/catalog.html', {
        'title': 'Рецепты',
        'recipes': recipes_data
    })

def add_page(request):
    return HttpResponse(f'Отображение рецептов с id')

def login(request):
    return HttpResponse(f'Отображение рецептов с id')


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")