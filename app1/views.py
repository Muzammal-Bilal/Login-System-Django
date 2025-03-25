from django.shortcuts import render, redirect    
from django.contrib.auth.models import User  
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url="login")
def Homepage(request):
    return render (request,'home.html')

def SignUpPage(request):
    if request.method=='POST':
        Uname=request.POST.get('username')
        Email=request.POST.get('email')
        Pass1=request.POST.get('password1')
        Pass2=request.POST.get('password2')

        if Pass1 != Pass2:
            messages.error(request, "Passwords do not match!")
            return redirect('signup')
        else:
            NewUser=User.objects.create_user(Uname,Email,Pass1)
            NewUser.save()
            return redirect('login') 


        

    return render (request,'signup.html')

def LoginPage(request):
    if request.method=='POST':
        Uname=request.POST.get('username')
        Pass1=request.POST.get('pass')
        user=authenticate(request,username=Uname,password=Pass1)
        if user is not None:
            login(request,user)
            return redirect("home")
        else:
             messages.error(request, "Invalid username or password!")


    return render (request,'login.html')
def LogoutPage(request):
    logout(request)
    return redirect("login")


