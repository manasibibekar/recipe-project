from django.db import models
from django.contrib.auth.models import User

class Recipe(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    recipe_name_model = models.CharField(max_length= 100)
    recipe_description_model = models.TextField() 
    recipe_image_model = models.ImageField(upload_to = 'recipe')
