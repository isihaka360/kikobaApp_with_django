<<<<<<< HEAD
# from django import forms
# from .models import Customer

# class RegistrationForm(forms.ModelForm):
#     class Meta:
#         model = Customer
#         fields = '__all__'
        
        
# class LoginForm(forms.ModelForm):
#     class Meta:
#         model = Customer
#         exclude = ['firstName','lastName']        
=======
from django import forms
from .models import Customer

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        
        
class LoginForm(forms.ModelForm):
    class Meta:
        model = Customer
        exclude = ['firstName','lastName']        
>>>>>>> b2866b4c11f91b0bba0d845cc1d316ca625a9e2d
        