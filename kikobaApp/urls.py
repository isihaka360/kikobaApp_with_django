from django.urls import path
from .views import home_view,register_view,login_view,user_dashboard_view , about_us_view , logout_view,kikoba_documentary,admin_dashboard_view

urlpatterns = [
    
    path('',home_view,name='home'),
    path('register/',register_view,name='register'),
    path('login/',login_view,name='login'),
    path('home/', user_dashboard_view, name='user_dashboard'),
    path('admini/',admin_dashboard_view, name='admin'),
    path('about/',about_us_view,name='about'),
    path('logout/',logout_view,name='logout'),
    path('upcoming events/' ,kikoba_documentary, name= 'documentary' ),
    
]
