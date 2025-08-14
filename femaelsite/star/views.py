from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.template.loader import render_to_string


def index(request):
    
    data = { 'title': 'Главная страница'}
    return render(request, 'star/index.html', data)

def about(request):
    return render(request, 'star/about.html', { 'title': 'О нас'})

def show_recipe(request, recipe_id): #сделать вызов для каждого рецепта
    return HttpResponse(f'Отображение рецептов с id = {recipe_id}')

def catalog(request):
    recipes_data = []
    
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