from django.contrib import admin

# Register your models here.
# I want to see the model so,for that first i have register it in admin.py
from .models import *


class MemberAdmin(admin.ModelAdmin):
    list_display = ["recipe_name","recipe_description","recipe_image"]
    
    
admin.site.register(Recipe,MemberAdmin)

