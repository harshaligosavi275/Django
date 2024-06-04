from django.contrib import admin

# Register your models here.
# I want to see the model so,for that first i have register it in admin.py
from .models import *


admin.site.register(Recipe)

