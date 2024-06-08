from django.db import models
from django.db import transaction
from django.db.models import F, Max
from django.contrib.auth.models import User

# Create your models here.
class Recipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    recipe_name = models.CharField(max_length=100)
    recipe_description = models.TextField()
    recipe_image = models.ImageField(upload_to="recipie_image")
    
 
def __str__(self):
    return f'{self.recipe_name} {self.recipe_description}{self.recipe_image}'
   
   
   
   
   
