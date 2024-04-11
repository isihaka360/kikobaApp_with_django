from django.urls import path
<<<<<<< HEAD
from .views import home_view,register_view,login_view,user_dashboard_view , about_us_view , logout_view,kikoba_documentary,admin_dashboard_view
=======
from .views import home_view,register_view,login_view,dashboard_view , about_us_view , logout_view, loan_Application_view,kikoba_investment_view,kikoba_documentary
>>>>>>> b2866b4c11f91b0bba0d845cc1d316ca625a9e2d

urlpatterns = [
    
    path('',home_view,name='home'),
    path('register/',register_view,name='register'),
    path('login/',login_view,name='login'),
<<<<<<< HEAD
    path('home/', user_dashboard_view, name='user_dashboard'),
    path('admini/',admin_dashboard_view, name='admin'),
    path('about/',about_us_view,name='about'),
    path('logout/',logout_view,name='logout'),
    path('upcoming events/' ,kikoba_documentary, name= 'documentary' ),
=======
    path('home/', dashboard_view, name='dashboard'),
    path('about/',about_us_view,name='about'),
    path('logout/',logout_view,name='logout'),
    path('upcoming events/' ,kikoba_documentary, name= 'documentary' )
>>>>>>> b2866b4c11f91b0bba0d845cc1d316ca625a9e2d
    
]
