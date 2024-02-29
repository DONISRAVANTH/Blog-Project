from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.forms import AuthenticationForm
from .models import CustomUser
from .forms import RegistrationForm


# Create your views here.

def Register_user(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
           user = form.save()
           login(request,user)
           return redirect('home-page')           
    else:
        form = RegistrationForm()
    return render (request,'signup.html', {'form':form})    

def Login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home-page')
        else:
            return HttpResponse('INCORRECT LOGIN DETAILS')           
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def Logout_user(request):
    logout(request)
    return redirect('home-page')

