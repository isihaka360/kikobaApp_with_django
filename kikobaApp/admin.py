from django.contrib import admin
from .models import Customer,CustomerProfile , Completed_Registration
                                                                                                                                                                                                                                                                     
# here we register our modelor database in admin penel
admin.site.register(Customer)
admin.site.register(CustomerProfile)
admin.site.register(Completed_Registration)