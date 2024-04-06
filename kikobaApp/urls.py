from django.urls import path
from .views import home_view,register_view,login_view,dashboard_view , about_us_view , logout_view, loan_Application_view,kikoba_investment_view,kikoba_documentary

urlpatterns = [
    
    path('loan_Applications/',loan_Application_view,name='loan'),
    path('kikoba_investment_Application/',kikoba_investment_view,name='investment'),
    path('',home_view,name='home'),
    path('register/',register_view,name='register'),
    path('login/',login_view,name='login'),
    path('home/', dashboard_view, name='dashboard'),
    path('about/',about_us_view,name='about'),
    path('logout/',logout_view,name='logout'),
    path('upcoming events/' ,kikoba_documentary, name= 'documentary' )
    
]
