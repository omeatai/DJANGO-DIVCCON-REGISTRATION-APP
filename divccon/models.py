from django.db import models
from django.contrib.auth.models import AbstractUser
from .choices import * 


class Province(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class User(AbstractUser):
    title = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    sex = models.CharField(choices=SEX_CHOICES, max_length=6)
    anglican = models.CharField(max_length=20)
    location = models.CharField(max_length=20) 
    province = models.ForeignKey(Province, on_delete=models.CASCADE, null=True, default=None) 
    diocese = models.CharField(max_length=50)
    church = models.CharField(max_length=50)
    designation = models.CharField(max_length=50)
    committee = models.CharField(max_length=50)
    user_photo = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.first_name.upper()} {self.last_name.upper()} - {self.username.upper()}"  
    

    
    
    
    