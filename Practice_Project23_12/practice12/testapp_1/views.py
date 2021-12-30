from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from .forms import StudentRegistration
from . models import Student
from django.contrib import messages
from django.views import View
# Create your views here.

def add_show(request):
    if request.method=='POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            fm.save()
            fm = StudentRegistration()

    else:
        fm = StudentRegistration()
    stud=Student.objects.all()

    return render(request,'testapp/addandshow.html',{'form':fm,'stud':stud})


def delete_view(request, id):
    if request.method=='POST':
        pi=Student.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/addandshow')


def update_view(request, id):
    if request.method=="POST":
        pi=Student.objects.get(pk=id)
        fm=StudentRegistration(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
            messages.add_message(request,messages.SUCCESS,'Update Successfully')


    else:
        pi=Student.objects.get(pk=id)
        fm=StudentRegistration(instance=pi)
        
    return render(request,'testapp/update.html',{'form':fm})
        

class Classbaseviews(View):
    def get(self,request):
        return HttpResponse('<h1>This response from class base views</h1>')




