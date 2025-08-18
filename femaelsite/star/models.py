from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
# from django.template.defaultfilters import slugify



class Category(models.Model):

    name = models.CharField(max_length=255, db_index=True, verbose_name = 'Категория')
    slug = models.SlugField(max_length=100, unique=True, db_index=True)

    class Meta:
        verbose_name = 'Категории'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
         return reverse('category', kwargs = {'cat_slug' : self.slug})
    
    
class recipe(models.Model):

    title = models.CharField(max_length = 255, verbose_name = 'Название')
    slug = models.SlugField(max_length = 255, unique = True, db_index = True, verbose_name = 'slug')
    game = models.CharField(max_length = 255, verbose_name = 'Название игры')
    ingredients = models.JSONField(default =list, blank = True, verbose_name = 'Ингредиенты')
    effect = models.CharField(max_length = 255, verbose_name = 'Эффект')
    preparation = models.CharField(max_length = 255, verbose_name = 'Способ приготовления')

    time_create = models.DateTimeField(auto_now_add = True, verbose_name = 'Время создания')
    time_update = models.DateTimeField(auto_now = True, verbose_name = 'Время изменение')

    cat = models.ForeignKey('Category', on_delete = models.PROTECT, verbose_name = 'Категория')

    author = models.ForeignKey(get_user_model(), on_delete = models.SET_NULL, related_name = 'post', null = True, default = None)

    class Meta: 
        verbose_name = 'Лучшие рецепты'
        verbose_name_plural = 'Лучшие рецепты'
        ordering = ['-time_create']
        indexes = [
            models.Index(fields = ['-time_create'])
        ]
    def get_absolute_url(self):
         return reverse('recipe', kwargs = {'recipe_slug' : self.slug})
    
    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.title)
    #     return super().save(*args, **kwargs)
    

