from django.shortcuts import render, redirect
from .models import *
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login

# set this to true after project is completed
# git config --global http.sslVerify true

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

        return redirect('home_name') # in redirect you keep the name of url

    if request.method == "GET":

        if request.GET.get('search_recipe_html'):
            queryset = Recipe.objects.all().filter(recipe_name_model__icontains = request.GET.get('search_recipe_html'))
        else:
            queryset = Recipe.objects.all()

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
    
def login_page(request): # rename from login to login_page because django built in function named login
    return render(request, "login.html")

def register(request):
    if request.method == "GET":
        return render(request, "register.html")
    
    elif request.method == "POST":
        requested_username = request.POST.get('register_username_html')
        existing_user = User.objects.filter(username=requested_username)

        if existing_user.exists():
            messages.error(request, "Username already taken. Try another one.")
            return redirect('register_name')
        
        else:
            user = User.objects.create(
                username = requested_username
            )
            user.set_password(request.POST.get('register_password_html')) # call this method to save encrypted password in db

            user.save()

            login(request, user)
            messages.success(request, f"{user.username} logged in successfully.")
            
            return redirect('home_name')