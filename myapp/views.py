from django.shortcuts import render
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from .forms import CustomUser, CustomAuthentication
from .models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.
@method_decorator(login_required(login_url='login'), name='dispatch')
class Home(View):
    def get(self,request):
        if request.user.is_authenticated:
            student=User.objects.get(email=request.user.email)
            return render(request, 'home.html', {'student': student})
        else:
            return redirect('login')

  
class Register(View):
    def get(self,request):
        Students=CustomUser()
        return render(request,'register.html',{'Students': Students})
    def post(self,request):
        Students=CustomUser(request.POST)
        if Students.is_valid():
            Students.save()
            return redirect('login')
        else:
            return render(request,'register.html',{'Students': Students})
        
class Login(View):
    def get(self,request):
        Students=CustomAuthentication()
        return render(request, 'login.html',{'Students' : Students})
    
    def post(self,request):
        Students=CustomAuthentication(data=request.POST)
        print("posst")
        if Students.is_valid():
            print("Valid")
            email=Students.cleaned_data.get('email')
            password=Students.cleaned_data.get('password')

            user=authenticate(request, email=email, password=password)
            print(email)
            print(password)
            print(user)
            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                Students.add_error(None, 'Inavlid email or Password')
                print("Auth Failed")
        else:
            print(Students.errors)
        return render(request,'login.html',{'Students':Students})
class Logout(View):
    def get(self,request):
        logout(request)
        return redirect('login')

