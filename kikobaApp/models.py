from django.db import models
# db panel of kikobaApp for handling data

# This is Customer model for Registered Users
# class Customer(models.Model):
#     firstName = models.CharField(max_length=255)
#     lastName = models.CharField(max_length=255)
#     email = models.EmailField(max_length=255)
#     password = models.CharField(max_length=10)
     
#     def __str__(self):
#         return f"{self.email} ({self.password})"
    
# # model for storing user profile uploaded from User dashboard 
# class CustomerProfile(models.Model):
#     Customer_image = models.ImageField()
#     Customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    
#     def __str__(self):
#         return f"{self.Customer}"
 
# # model for holding data submited from user dashboard to complete registration
# class Completed_Registration(models.Model):
#     full_name = models.CharField(max_length=255)    
#     email = models.EmailField(max_length=255)
#     date_birth = models.DateTimeField(auto_now_add=True)
#     date_joined = models.DateTimeField(auto_now_add=True)
#     phone_number = models.IntegerField()
#     Customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    
#     def validation_email(self):
#         pass
    
#     def __str__(self):
#         return f"{self.full_name} ({self.phone_number})"
 
 
