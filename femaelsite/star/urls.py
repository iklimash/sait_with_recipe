from django.urls import path
from . import views




urlpatterns = [

    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('catalog/', views.catalog, name='catalog'),
    path('recipe/<slug:recipe_slug>/', views.show_recipe, name='recipe'),
    path('addpage/', views.add_page, name='addpage'),
    path('login/', views.login, name='login'),
    path('category/<slug:cat_slug/>', views.show_category, name = 'category'),

]