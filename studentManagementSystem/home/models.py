from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=18)
    email = models.EmailField(null=True)
    address = models.TextField(null=True,blank=True)
    phone = models.IntegerField(null=True)
    
    # image = models.ImageField()
    # file = models.FileField()
    
    
    
    def __str__(self):
        return f'{self.name} {self.age} {self.email} {self.address}' 