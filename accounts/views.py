from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.
def logout(request):
    auth.logout(request)
    return redirect('/')
def login(request):
    if request.method == "POST":
        username = request.POST["UserName"]
        password = request.POST["Password"]
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Invalid Credentials")
            return redirect('login')
    else:
        return render(request,"login.html")

def register(request):
    if request.method == "POST":
        FirstName = request.POST["FirstName"]
        LastName = request.POST["LastName"]
        UserName = request.POST["UserName"]
        Password = request.POST["Password"]
        Email = request.POST["Email"]
        ConfirmPassword = request.POST["ConfirmPassword"]
        if Password == ConfirmPassword:
            if User.objects.filter(username=UserName).exists():
                messages.info(request,"User already exists")
                return redirect('register')
            elif User.objects.filter(email=Email).exists():
                messages.info(request,"Email exists")
                return redirect('register')
            else:
                user = User.objects.create_user(first_name=FirstName,last_name=LastName,username=UserName,password=Password,email= Email)
                user.save();
                messages.info(request,"User Registered")
                return redirect('/')
        else:
            messages.info(request,"Password Not Matching")
            return redirect('register')
    else:
        return render(request,"register.html")
    

