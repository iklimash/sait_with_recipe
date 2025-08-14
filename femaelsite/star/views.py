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
    context = {
        'recipes': recipes,
        'title': 'Каталог рецептов'  # Жёстко заданный заголовок
    }
    return render(request, 'star/catalog.html', context)

def show_category(request, cat_slug):

    category = get_object_or_404(Category, slug = cat_slug)
    recipes = recipe.objects.filter(category=category)

    recipe_data ={
            'id': category.id,
            'title': f'Рубрика:{category.name}',
            'game': category.game,
            'ingredients': category.ingredients,  
            'effect': category.effect,
            'preparation': category.preparation,
            'cat_selected': category.pk,
    }
    context = {
        'recipe': recipe_data,
        'recipes': recipes,  
        'title': category.title,
        'categories': Category.objects.all(),
    }

    return render(request, 'star/category.html', context)

def add_page(request):
    return HttpResponse(f'Отображение рецептов с id')

def login(request):
    return HttpResponse(f'Отображение рецептов с id')


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")