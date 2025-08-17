from django.contrib import admin
from .models import recipe, Category

@admin.register(recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create')
    list_display_links = ('id', 'title')
    ordering = ['time_create','title']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    ordering = ['id']
# admin.site.register(recipe, RecipeAdmin)

