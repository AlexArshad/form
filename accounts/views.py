from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User, auth
from django.shortcuts import render, get_object_or_404, redirect
from .models import Main
from .models import AuthUser
from django.apps import AppConfig
from django.contrib.auth import authenticate,  login, logout
from django.contrib.auth.decorators import login_required
from accounts.forms import LoginForm

# create your views here

def home_view(request):
    sitename = "User Reg Form"

    return render(request, 'front/basic.html', {'sitename' : sitename})


def signup_view(request):
    if request.method =='POST':
         username = request.POST['username']
         first_name = request.POST['first_name']
         last_name = request.POST['last_name']
         email = request.POST['email']
         password = request.POST['password']
         #password1 = request.POST['password1']

         user = User.objects.create_user(username = username , first_name = first_name, last_name = last_name , email = email, password = password  )#, password2 = password2 ,  password2 = password2
         user.save()
         return redirect('/')

    else:
        return render(request, 'front/signup.html',)


def login_view(request):
    return render(request, 'front/login.html')

def results_view(request):
    data = request.GET['textarea']
    data1 = request.GET['textarea1']
    return render(request, 'front/results.html', {'data' : data , 'data1' : data1})

def panel_view(request):
    return render(request, 'back/index.html')

def user_show(request):
    marks_data = AuthUser.objects.all()
        
    return render(request, 'back/user.html', {'marks_data' : marks_data})
 
def mylogin_view(request):

    if request.method == 'POST' :

        username = request.POST.get('username')
        password = request.POST.get('password')
     
        user = authenticate(username=username, password=password)
        return redirect('/')

    else:    
        return render(request, 'registrations/adminindex.html')

def form_view(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        count = AuthUser.objects.filter(username=username, password=password).count()
        if count > 0:
            return redirect('/panel')

    return render(request, 'front/form.html')

