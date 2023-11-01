from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from app.models import ContactU
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(requst):
    return render(requst,"home.html")

def home1(request):
    return render(request,"home.html")


def contactus(request):
    return render(request,"contactus.html")


def signup(request):
    return render(request,"auth/signup.html")
    # return HttpResponse("signup")


def savedata(request):
    if request.method == "POST":
        # return HttpResponse("saved")
        Username = request.POST.get("username")
        Firstname = request.POST.get("fname")
        Lastname = request.POST.get("lname")
        Email = request.POST.get("email")
        Password = request.POST.get("password")

        userinfo = User.objects.create_user(username = Username, first_name = Firstname, last_name = Lastname, email = Email, password = Password)
        userinfo.save()
        return redirect("signup")
    return HttpResponse("data saved")


def saveinfo(request):
    if request.method == "POST":
        name = request.POST.get("Nname")
        Phone = request.POST.get("Pnumber")
        Email = request.POST.get("Eemail")
        Message = request.POST.get("Mmessage")

        info = ContactU.objects.create(Name = name, phone_number = Phone, Email = Email, message = Message)
        info.save()
        return redirect("home")
    return HttpResponse("data saved")

# ----------------------------------->
@login_required(login_url="/loginn")
def products(request):
    return render(request, "products.html")




def loggedin(request):
    if request.method == "POST":
        x = request.POST.get("username")
        y = request.POST.get("password")

        user = authenticate(username = x, password = y)

        if user is not None:
            login(request, user)

        return render(request, "products.html")


    return render(request, "home.html")

def loginn(request):
    return render(request, "auth/login.html")


def logoutuser(request):
    logout(request)
    return redirect("home")



def showdata(request):
    data = ContactU.objects.all()
    return render(request, "showdata.html", {"data" : data})

def updatedata(request, x):
    data = ContactU.objects.get(id = x)
    return render(request, "update.html", {"data" : data})

def update(request , x):
    x = ContactU.objects.get(id = x)
    if request.method == "POST":
        name = request.POST.get("Nname")
        Phone = request.POST.get("Pnumber")
        Email = request.POST.get("Eemail")
        Message = request.POST.get("Mmessage")

        x.Name = name
        x.phone_number = Phone
        x.Email = Email
        x.message = Message
        x.save()

        return redirect("showdata")
    return HttpResponse("data saved")


def detethis(request, x):
    x = ContactU.objects.get(id = x)
    x.delete()
    return redirect("showdata")

