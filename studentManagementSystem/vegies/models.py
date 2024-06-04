from django.db import models
from django.db import transaction
from django.db.models import F, Max

# Create your models here.
class Recipe(models.Model):
    recipe_name = models.CharField(max_length=100)
    recipe_description = models.TextField()
    recipe_image = models.ImageField(upload_to="recipie_image")
    
    