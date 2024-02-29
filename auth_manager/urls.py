from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.Login_user,name='login-page'),
    path('registration/',views.Register_user,name='register-page'),   
    path('logout/',views.Logout_user,name='logout-page'),
]