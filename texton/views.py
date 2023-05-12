from django.shortcuts import render,redirect
from django.http import HttpResponse
from texton.models import Student
from texton.forms import StudentForm, EmployeeForm


def TEXTON(request):
    return render(request,'TEXTON.html')
def makepurchase(request):
    return render(request,'makepirchase.html')
def cat(request):
    return render(request, 'cat.html')
def Jacaranda(request):
      return render(request,'Jacaranda.html')

def members(request):
    all=Student.objects.all().values()
    details={
        'members':all
    }
    return render(request,'members.html',details)

def student(request):
    stu = StudentForm()
    return render(request,'student.html',{'form':stu})

def Employee(request):
   if request.method=="post":
       form= EmployeeForm(request.post)
       if form.is_valid():
           form.SAVE()
           return redirect("/")
   else:
      form=EmployeeForm()
      return render(request,'employee.html',{'form':form})

def setsession(request):
    request.session['firstname']='Mbappe'
    request.session['lastname']='John'
    request.session['email']='wekesajohn610@gmail.com'
    return HttpResponse('session has been successfully created')
def getsession(request):
    fname = request.session['firstname']
    lname = request.session['lastname']
    emailaddress = request.session['email']
    return HttpResponse(fname + ' ' + lname+' ' + emailaddress)

def form(request):
    return render(request,'creatform.html')

def power(request):
    return render(request,'power.html')
# Create your views here.
