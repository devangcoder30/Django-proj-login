from django.shortcuts import render,redirect,  HttpResponse
from .models import Student
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')

def index(request):
    stud=Student.objects.all()
    print(stud)
    return render(request, 'show.html', {'stu': stud})

def home(request):
    if request.method=='POST':
        name=request.POST['name']
        fname=request.POST['fname']

        student=Student(name=name,fname=fname)
        student.save()
    return render(request, 'index.html')

def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('pass')

        myuser=User.objects.create_user(uname,email,password)
        myuser.save()
        return redirect('login')
        # return HttpResponse("HIIIII")
    return render(request, 'singup.html')

def LoginPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        password=request.POST.get('pass')

        user=authenticate(request,username=uname,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse("Galat hai")

    return render(request, 'login.html')

def logoutf(request):
    logout(request)
    return render(request,'login.html')

