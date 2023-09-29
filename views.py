from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    return render(request,'index.html')
def login(request):
    return render(request,'login.html')
def register(request):
    return render(request,'register.html')
def blog(request):
    return render(request,'blog.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
def exhibition(request):
    return render(request,'exhibition.html')
def competition(request):
    return render(request,'competition.html')
def artstore(request):
    return render(request,'artstore.html')



def contact(request):
    return render(request,'contact.html')
def login(request):
    return render(request,'login.html')
    if request.method == "POST":
        email=request.POST['email']
        password=request.POST['password']
        user=authenticate(email=email,password=password)
        if user is not None:
            login(request,user)

            return HttpResponse('login')
        else:
                return redirect('register')
def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        myuser = User.objects.create_user(username,email,password)
        myuser.save()
        return redirect('login')
    return render(request,'register.html')
    

