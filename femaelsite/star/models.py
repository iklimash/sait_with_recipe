from django.db import models
from django.urls import reverse


class recipe(models.Model):

    title = models.CharField(max_length = 255, verbose_name = 'Название')
    slug = models.SlugField(max_length = 255, unique = True, db_index = True, verbose_name = 'slug')
    game = models.CharField(max_length = 255, verbose_name = 'Название игры')
    ingredients = models.JSONField(default =list, blank = True, verbose_name = 'Ингредиенты')
    effect = models.CharField(max_length = 255, verbose_name = 'Эффект')
    preparation = models.CharField(max_length = 255, verbose_name = 'Способы приготовления')

    time_create = models.DateTimeField(auto_now_add = True, verbose_name = 'Время создания')
    time_update = models.DateTimeField(auto_now = True, verbose_name = 'Время изменение')

    cat = models.ForeignKey('Category', on_delete = models.PROTECT, verbose_name = 'Категория')

    class Meta: 
        verbose_name = 'Лучшие рецепты'
        verbose_name_plural = 'Лучшие рецепты'
        ordering = ['time_create']
        indexes = [
            models.Index(fields = ['time_create'])
        ]
    def get_absolute_url(self):
         return reverse('recipe', kwargs = {'recipe_slug' : self.slug})
    
class Category(models.Model):

    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=100, unique=True, db_index=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
         return reverse('category', kwargs = {'cat_slug' : self.slug})
