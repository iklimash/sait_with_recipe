from django.urls import path
from . import views
from users.views import login_user




urlpatterns = [

    path('', login_user, name='login'),
    path('/home', views.indexHome.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('catalog/', views.catalog, name='catalog'),
    path('recipe/<slug:recipe_slug>/', views.show_recipe, name='recipe'),
    path('addpage/', views.add_page.as_view(), name='addpage'),
    path('recipes/', views.all_recipes, name='all_recipes'),
    path('category/<slug:cat_slug>/', views.show_category, name='category'),
    path('edit/<int:pk>/', views.UpdatePage.as_view(), name='update'),

]