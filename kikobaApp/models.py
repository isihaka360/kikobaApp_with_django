from django.db import models
from django.contrib.auth.models import Permission ,Group
from django.contrib.auth.models import AbstractUser
# db panel of kikobaApp for handling data

class Customer(models.Model):
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=10)
    
    group = models.ManyToManyField(Group,related_name='Customer_group')
    User_permission = models.ManyToManyField(Permission, related_name='User_Customer_permission')
    
    def __str__(self):
        return f"{self.email} ({self.password})"
 
