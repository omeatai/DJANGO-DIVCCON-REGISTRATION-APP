from django.db import models
from django.contrib.auth.models import AbstractUser
from .choices import * 


class User(AbstractUser):
    first_name = models.CharField(max_length=50, unique=False)
    last_name = models.CharField(max_length=50, unique=False)
    password = models.CharField(max_length=200, unique=True)
    username = models.CharField(max_length=50, unique=False, default="NONE")
    email = models.EmailField(max_length=50, unique=False)
    title = models.CharField(max_length=50, unique=False)
    phone = models.CharField(max_length=20, unique=False)
    sex = models.CharField(choices=SEX_CHOICES, max_length=6)
    anglican = models.CharField(choices=ANGLICAN_CHOICES, max_length=20)
    location = models.CharField(choices=LOCATION_CHOICES, max_length=20) 
    province = models.CharField(choices=PROVINCE_CHOICES, max_length=50, default="NONE") 
    diocese = models.CharField(max_length=50, default="NONE")
    church = models.CharField(max_length=50, default="NONE")
    designation = models.CharField(max_length=50, default="DELEGATE")
    committee = models.CharField(max_length=50, default="NONE")
    # photo = models.ImageField(upload_to='images/', default="NONE", null=True, blank=True)
    photo = models.ImageField(upload_to='images/')
    
    def __str__(self):
        return f"{self.first_name.upper()} {self.last_name.upper()} - {self.username.upper()}"  




