from django.db import models


class recipe(models.Model):

    title = models.CharField(max_length = 255)
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
 