from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.template.loader import render_to_string

from .models import Category, recipe


def index(request):
    
    data_index = { 'title': 'Главная страница'}
    return render(request, 'star/index.html', data_index)

def about(request):
    return render(request, 'star/about.html', { 'title': 'О нас'})

def show_recipe(request, recipe_slug):
    recipe_obj  = get_object_or_404(recipe, slug = recipe_slug)

    recipe_data ={
            'id': recipe_obj.id,
            'title': recipe_obj.title,
            'game': recipe_obj.game,
            'ingredients': recipe_obj.ingredients,  
            'effect': recipe_obj.effect,
            'preparation': recipe_obj.preparation,
            'cat': recipe_obj.cat,
    }
    context = {
        'recipe': recipe_data,
        'title': recipe_obj.title,  # Add this line
    }
    return render(request, 'star/recipe.html', context)

def catalog(request):
    recipes = recipe.objects.all()  
    categories = Category.objects.all()
    context = {
        'recipes': recipes,
        'categories': categories,
        'cat_selected': None,
        'title': 'Лучшие рецепты'
    }
    return render(request, 'star/catalog.html', context)

def show_category(request, cat_slug):
    category = get_object_or_404(Category, slug=cat_slug)
    recipes = recipe.objects.filter(cat=category)
    context = {
        'recipes': recipes,
        'categories': Category.objects.all(),
        'cat_selected': category.pk,
        'title': f'Рубрика: {category.name}',
    }
    return render(request, 'star/catalog.html', context)

def all_recipes(request):
    recipes = recipe.objects.all()
    return render(request, 'star/catalog.html', {
        'recipes': recipes,
        'categories': Category.objects.all(),
        'cat_selected': None,
        'title': 'Лучшие рецепты'
    })

def add_page(request):
    return HttpResponse(f'Отображение рецептов с id')

def login(request):
    return HttpResponse(f'Отображение рецептов с id')


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")