from django.shortcuts import render , redirect
from django.contrib.auth.hashers import make_password
# from .models import Customer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# view controlling panel
def callback_requuests(request):
    # handling callback requests
    pass
def kikoba_documentary(request):
    return render(request, 'kikobaApp/events.html')
<<<<<<< HEAD
def user_dashboard_view(request):
    return render(request, 'kikobaApp/user_dash.html')
def admin_dashboard_view(request):
    return render(request, 'kikobaApp/admin_dash.html')
=======
def kikoba_investment_view(request):
    # logics for investment
    return render(request, 'kikobaApp/investment.html')

def loan_Application_view(request):
    # handling loan application requests
    return render(request, 'kikobaApp/loan_Application.html')
>>>>>>> b2866b4c11f91b0bba0d845cc1d316ca625a9e2d

def about_us_view(request):
    return render(request,'kikobaApp/about.html')

def home_view(request):
    return render(request,'kikobaApp/home.html')

def register_view(request):
    
    """ This function handles registration and
       The function accepts the POST request with four arguments as
       username, email , password and confirmed password
       The function uses the make_password method for password Encryption """
       
    if request.method == 'POST':
        
        username = request.POST['username']
        email     = request.POST['email']
        password  = request.POST['password']
        confirmed_password = request.POST['confirmed_password']
        
        # checking validity of password and confirmed password
        if password == confirmed_password:
            hash_password = make_password(password)
<<<<<<< HEAD
            user = User.objects.create_user( username = username , email=email , password=hash_password )
            user.save()
            # messages.success(request , 'Registration successful')
            # user is redirected to login page
=======
            
            user = Customer.objects.create(firstName=firstName, lastName=lastName, email=email , password=hash_password)
            user.save()
>>>>>>> b2866b4c11f91b0bba0d845cc1d316ca625a9e2d
            return redirect('login')
            
        else:
            # messages.error(request , 'Registration failed please try again!')
            return render (request,'kikobaApp/register.html',{'error_message':'password do not match'})
    else:
        return render(request,'kikobaApp/register.html')
    
<<<<<<< HEAD

def login_view(request):
     """ This function handles Login Mechanism
       The function accepts the POST request with two arguments as
       emailAddress and password 
       The function works together with the authenticate method and login method
       authenticate method: work for authenticate the user
       login method: is called when the user is authenticated the redirect the user into the login page"""
       
     if request.method == 'POST':
            
            username = request.POST.get('username')
            pass1 = request.POST.get('password')
            
            # Authenticate user
            user = authenticate(request , username = username, password = pass1)
             
            if user is not None:
                # User authentication successful
                login(request, user)
                return render(request, 'kikobaApp/admin_dash.html')
            else:
                # Invalid email or password
                return render(request, 'kikobaApp/login.html', {'error_message': 'Invalid email or password.'})
     else:
            # GET request, render login page
            return render(request, 'kikobaApp/login.html')     
=======
# def login_view(request):
    
#     if request.method == 'POST':
#        email = request.POST.get('email')
#        password = request.POST.get('password')
#        user = authenticate(request,email=email, password=password)
#        if user is not None:
#         login(request, user)
#         return redirect('dashboard')
    
#        else:
         
#          return render(request, 'kikobaApp/login.html', {'error_message': 'Invalid email or password.'})
     
#     else:
        
#         return render(request, 'kikobaApp/login.html')  

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        # Authenticate user
        user = authenticate(request, email = email, password = password)
        print(user)
        
        if user is not None:
            # User authentication successful
            login(request, user)
            return redirect('dashboard')
        else:
            # Invalid email or password
            return render(request, 'kikobaApp/login.html', {'error_message': 'Invalid email or password.'})
    else:
        # GET request, render login page
        return render(request, 'kikobaApp/login.html')     
>>>>>>> b2866b4c11f91b0bba0d845cc1d316ca625a9e2d
    
def logout_view(request):
    return redirect('login')   
            
@login_required(login_url='login')
def dashboard_view(request):
    return render(request,'kikobaApp/user_dash.html')
    
