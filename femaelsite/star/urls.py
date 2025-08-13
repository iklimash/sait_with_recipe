from django.urls import path
from . import views




urlpatterns = [

    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('catalog/', views.catalog, name='catalog'),
    path('recipe/<int:recipe_id>/', views.show_recipe, name='recipe'),
]