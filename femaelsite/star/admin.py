from django.contrib import admin
from .models import recipe, Category

@admin.register(recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'time_create', 'cat', 'brief_info')
    list_display_links = ('title',)
    ordering = ['time_create','title']
    list_editable = ('cat',)
    search_fields = ['title', 'cat__name']
    list_filter = ['cat__name']
    prepopulated_fields = {"slug":("title",)}

    @admin.display(description="Краткое описание")
    def brief_info(self, recipe: recipe):
        return f"Описание {len(recipe.effect)} символов"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    ordering = ['id']
# admin.site.register(recipe, RecipeAdmin)

