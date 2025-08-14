from django.db import models
from django.urls import reverse


class recipe(models.Model):

    title = models.CharField(max_length = 255)
    slug = models.SlugField(max_length = 255, unique = True, db_index = True)
    game = models.CharField(max_length = 255)
    ingredients = models.JSONField(default =list, blank = True)
    effect = models.CharField(max_length = 255)
    preparation = models.CharField(max_length = 255)

    time_create = models.DateTimeField(auto_now_add = True)
    time_update = models.DateTimeField(auto_now = True)

    class Meta: 
        ordering = ['time_create']
        indexes = [
            models.Index(fields = ['time_create'])
        ]
    def get_absolute_url(self):
         return reverse('recipe', kwargs = {'recipe_slug' : self.slug})