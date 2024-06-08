from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from vegies.models import *

# Create your views here.


@login_required(login_url='/login/')
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


@login_required(login_url='/login/')
def show_recipe(request):
    data =  Recipe.objects.all().values()
    # print(data)
    return render(request, "recipe_table.html", context={"data":data})

# ----------------------------delete recipe----------------------------------------


@login_required(login_url='/login/')
def delete_Recipe(request,id):
        deleteRecipe = Recipe.objects.get(id=id)
        deleteRecipe.delete()
        return redirect('/recipes/')
    
# -------------------------update recipe----------------------------------------


@login_required(login_url='/login/')
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
  

# ---------------------------authentication-------------------------------
def login_page(request):
    if request.method =="POST":
        data = request.POST
        username = data.get('username')
        password = data.get('password')
        
       
        if not User.objects.filter(username = username).exists():
            messages.info(request,"Invalid username..")
            return redirect('/login/')
        
        user = authenticate(username=username, password=password)
        if user is None:
            messages.info(request,"Invalid password..")
            return redirect('/login/')
        else:
            login(request,user)
            return redirect('/recipes/')
        
    context = {"page_title":"login page"}
    return render(request, "login.html",context)

# -----------------------------------------------------------------------------

def log_out(request):
   logout(request)
   return redirect('/login/')


# -------------------------------------------------------------------------------------
def register_page(request):
    
    if request.method =="POST":
        data = request.POST
        first_name = data.get('first_name')   # or we can do like this also, request.POST.get('firstname')
        last_name = data.get('last_name')
        username = data.get('username')
        password = data.get('password')
        # print(firstname,lastname,username,password)
        
        
        user = User.objects.filter(username=username)
        if user.exists():
           messages.info(request,'Username already taken..')
           return redirect('/register/')
        
        user = User.objects.create(first_name=first_name,
                                    last_name = last_name,
                                    username = username
                                    )
        user.set_password(password)
        user.save()
        
        messages.info(request,'Account created successfully..')
        return redirect('/register/')
    
    context = {"page_title":"Register page"}
    return render(request, 'register.html',context)
