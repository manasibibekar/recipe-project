from django.shortcuts import render, redirect
from .models import *
from django.shortcuts import get_object_or_404

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

        return redirect('home_name') # in redirect you keep the name

    if request.method == "GET":
        queryset = Recipe.objects.all()
        print(queryset)
        context = {"recipes": queryset}
        return render(request, "recipes.html", context)
    
def delete_recipe(request, id):
    recipe = Recipe.objects.get(id=id)
    recipe.delete()
    return redirect('home_name')

def update_recipe(request, id):
    if request.method == "GET":
        recipe = Recipe.objects.get(id=id)
        context = {"recipe": recipe}
        return render(request, "update.html", context)
    
    if request.method == "POST":
        recipe = get_object_or_404(Recipe, id=id)
        recipe.recipe_name_model = request.POST.get('update_recipe_name_html')
        recipe.recipe_description_model = request.POST.get('update_recipe_description_html')
        recipe.recipe_image_model = request.FILES.get('update_recipe_image_html')

        recipe.save()

        return redirect('home_name')