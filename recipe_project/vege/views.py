from django.shortcuts import render, redirect
from .models import *

def recipes(request):
    if request.method == "POST":
        data = request.POST
        # print(data)
        recipe_name = data.get('recipe_name_html')
        recipe_description = data.get('recipe_description_html')
        recipe_image = request.FILES.get('recipe_image_html')
        # print(recipe_image, recipe_name, recipe_description)

        Recipe.objects.create(
            recipe_name_model = recipe_name,
            recipe_description_model = recipe_description,
            recipe_image_model = recipe_image
        )

        return redirect('/recipes/')

    return render(request, 'recipes.html')
