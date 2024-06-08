from django.contrib import admin
from home.models import Student
# Register your models here.


# Set list_display
class MemberAdmin(admin.ModelAdmin):
    list_display =["name","age","email","address","phone"]


admin.site.register(Student,MemberAdmin)