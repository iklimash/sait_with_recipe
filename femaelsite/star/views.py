from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, UpdateView
from .forms import AddPostForm
from django.core.paginator import Paginator
from .models import Category, recipe

class indexHome(TemplateView):
    template_name = 'star/index.html'
    extra_context = { 'title': 'Главная страница'}

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
    paginator = Paginator(recipes, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    categories = Category.objects.all()
    context = {
        'page_obj': page_obj,
        'categories': Category.objects.all(),
        'cat_selected': None,
        'title': 'Лучшие рецепты',
        
    }
    return render(request, 'star/catalog.html', context)

def show_category(request, cat_slug):
    category = get_object_or_404(Category, slug=cat_slug)
    recipes = recipe.objects.filter(cat=category)
    paginator = Paginator(recipes, 6)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'recipes': recipes,
        'categories': Category.objects.all(),
        'cat_selected': category.pk,
        'title': f'Рубрика: {category.name}',
        'page_obj': page_obj
    }
    return render(request, 'star/catalog.html', context)

def all_recipes(request):
    recipes = recipe.objects.all()
    paginator = Paginator(recipes, 6)  # Добавляем пагинацию
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'star/catalog.html', {
        'page_obj': page_obj,  
        'categories': Category.objects.all(),
        'cat_selected': None,
        'title': 'Лучшие рецепты'
    })

class add_page(View):
    
    def get(self, request):
        form = AddPostForm()
        data = {
        'title': 'Добавление рецепта',
        'form': form
        }
        return render(request, 'star/addpage.html', data)

    def post(self, request):
        form = AddPostForm(request.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            try:
                recipe.objects.create(**form.cleaned_data)
                return redirect('catalog')
            except:
                form.add_error(None, "Ошибка добавления рецепта")
        data = {
        'title': 'Добавление рецепта',
        'form': form
        }
        return render(request, 'star/addpage.html', data)
    
class UpdatePage(UpdateView):
    
    model = recipe
    fields = ['title', 'slug', 'game', 'ingredients', 'effect', 'preparation', 'cat']
    template_name = 'star/addpage.html'
    success_url = reverse_lazy('home')
    extra_context = {'title': 'Изменение рецепта'}

def login(request):
    return HttpResponse("<h1>Авторизация</h1>")

def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")