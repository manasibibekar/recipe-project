from django.db import models

class Recipe(models.Model):
    recipe_name_model = models.CharField(max_length= 100)
    recipe_description_model = models.TextField() 
    recipe_image_model = models.ImageField(upload_to = 'recipe')
