from django.http import HttpResponseRedirect
from django.shortcuts import render
from . forms import StudentRegistration
from . forms import Student_Registration


# Create your views here.
def show_formdata(request):
    if request.method=='POST':
        fm=StudentRegistration(request.POST)
        if fm.is_valid():
            print('form valid')
    else:
        fm=StudentRegistration()
    return render(request,'testapp/home.html',{'form':fm})
# ************************************************************************
# 2]-----------------------------
from . models import UserM
from .forms import Signupform
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout


def student_view(request):
    if request.method == 'POST':
        # pi=User.objects.get(pk=1)
        fm=Student_Registration(request.POST)
        if fm.is_valid():
            ab=fm.cleaned_data['name']
            bc=fm.cleaned_data['email']
            cd=fm.cleaned_data['password']
            reg=UserM(name=ab,email=bc,password=cd)
            reg.save()

    else:
        fm=Student_Registration()

    return render(request,'testapp/info.html',{'form':fm})


def signup_views(request):
    if request.method == 'POST':
        ab=Signupform(request.POST)
        if ab.is_valid():
            ab.save()
    else:
        ab=Signupform()

    return render(request,'testapp/signup.html',{'signup':ab})


def user_login(request):
    if request.method=='POST':
        fm=AuthenticationForm(request=request,data=request.POST)
        if fm.is_valid():
            uname=fm.cleaned_data['username']
            upass=fm.cleaned_data['password']
            user=authenticate(username=uname,password=upass)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/profile')
    else:
        fm=AuthenticationForm()

    return render(request,'testapp/login.html',{'form':fm})


def profile_view(request):
    return render(request,'testapp/profile.html')

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/login')




