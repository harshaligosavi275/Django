from django.shortcuts import render,redirect,HttpResponse
from vegies.models import *

# Create your views here.
def recipes(request):
    if request.method == "POST":
        # for text data
         data = request.POST
         recipe_name = data.get('recipe_name')
         recipe_description = data.get('recipe_description')
         
        #  for files data we have to do like this,
         recipe_image = request.FILES.get('recipe_image')
         
         print(recipe_name)
         print(recipe_description)
         print(recipe_image)
         
        # ----------- i will insert the data in Model(table)-----------
        #  Recipe.objects.create(
        #      recipe_name = recipe_name, 
        #      recipe_description = recipe_description,
        #      recipe_image = recipe_image
        #      )
        #  ----------or we can add like this----------------
         recipe = Recipe(recipe_name=recipe_name,recipe_description=recipe_description,recipe_image=recipe_image)
         recipe.save()
     
         return redirect('/recipes/')
     
    # ---------------functionality: search recipe by its name------------------------------------
    querySet = Recipe.objects.all()
    if request.GET.get('search'):
              # print(request.GET.get('search'))
              querySet = querySet.filter( recipe_name__icontains = request.GET.get('search') )
              
    context = {"recipe":querySet}    
    # ------------------------------------------------------------------------------------------         
    return render(request, "recipes.html",context)



# ----------------------------show all recipes------------------------------------


def show_recipe(request):
    data =  Recipe.objects.all().values()
    # print(data)
    return render(request, "recipe_table.html", context={"data":data})

# ----------------------------delete recipe----------------------------------------

def delete_Recipe(request,id):
        deleteRecipe = Recipe.objects.get(id=id)
        deleteRecipe.delete()
        return redirect('/recipes/')
    
# -------------------------update recipe----------------------------------------

def update_Recipe(request,id):
      updateRecipe = Recipe.objects.get(id=id)
      if request.method == "POST":
          # for text data
         data = request.POST
         recipe_name = data.get('recipe_name')
         recipe_description = data.get('recipe_description')
         
        #  for files data we have to do like this,
         recipe_image = request.FILES.get('recipe_image')
         
         updateRecipe.recipe_name = recipe_name
         updateRecipe.recipe_description = recipe_description
         updateRecipe.recipe_image = recipe_image
         updateRecipe.save()
         
         return redirect('/recipes/')
      return render(request, "update_recipe.html",context={"updateRecipe":updateRecipe})
  
