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
    recipes_data = [
        {
            'id': '1',
            'title': 'Зелье стойкости',
            'game': 'The Witcher 3',
            'ingredients': ['1x Белоголов', '1x Копытень', '1x Растопша'],
            'effect': '+25% к сопротивлению ядам и +500 к макс. здоровью',
            'preparation': 'Смешать в алхимическом наборе при лунном свете'
        },
        {
            'id': '2',
            'title': 'Суп из глаз краба',
            'game': 'Monster Hunter',
            'ingredients': ['2x Глаза краб-паука', '1x Острый перец'],
            'effect': '+15 к защите и иммунитет к снежному замедлению',
            'preparation': 'Варить в котле 10 минут до помутнения жидкости'
        },
        {
            'id': '3',
            'title': 'Тыквенный пирог',
            'game': 'Stardew Valley',
            'ingredients': ['1x Тыква', '1x Пшеничная мука', '1x Сахар'],
            'effect': '+50 к энергии и +2 к скорости',
            'preparation': 'Выпекать в печи 4 часа при 180°C'
        },
        {
        'id': '5',
        'title': 'Эликсир ярости',
        'game': 'Skyrim',
        'ingredients': [
            '1x Кровь тролля',
            '2x Корень мандрагоры',
            '1x Огненный соль'
        ],
        'effect': '+30% к урону в ближнем бою на 5 минут',
        'preparation': 'Варить в железном котле до появления красных паров'
        },
        {
        'id': '6',
        'title': 'Пирог с паучьими глазами',
        'game': 'Divinity: Original Sin 2',
        'ingredients': [
            '3x Глаз гигантского паука',
            '1x Мука',
            '2x Яйца пещерной птицы'
        ],
        'effect': 'Иммунитет к ядам на 1 час',
        'preparation': 'Выпекать в печи 2 часа при 200°C'
        }
    ]
    
    return render(request, 'star/catalog.html', {
        'title': 'Рецепты',
        'recipes': recipes_data
    })

def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")