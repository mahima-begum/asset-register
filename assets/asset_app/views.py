from contextlib import redirect_stderr
from importlib.metadata import requires
from operator import truediv
from webbrowser import get
from xmlrpc.client import DateTime
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from asset_app.models import Asset
from asset_app.forms import AssetForm
import re
import datetime

# Create your views here.
def home(request):
    return render(request, "asset_app/signin.html")

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        forename = request.POST["forename"]
        surname = request.POST["surname"]
        email = request.POST["email"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]
        admin = convert_to_bool(request.POST.get('admin', False))

        if User.objects.filter(username=username):
            messages.error(request, "Username already exists. Please enter a different username.")
            return redirect("register")

        if User.objects.filter(email=email):
            messages.error(request, "Email already registered.")            
            return redirect("register")

        if len(username)>15:
            messages.error(request, "Username must be less than 15 characters.")            
            return redirect("register")

        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return redirect("register")
        
        if not username.isalnum():
            messages.error(request, "Username must be alphanumeric.")
            return redirect("register")

        if len(password1) < 10:
            messages.error(request, "Password must be greater than 10 characters.")
            return redirect("register")

        if not re.match(r"^(?=.{6,20}$)\D*\d", password1):
            messages.error(request, "Password must contain at least 1 number.")
            return redirect("register")

        if not re.match(r"(?=.*[a-z])", password1):
            messages.error(request, "Password must contain at least 1 lowercase letter.")
            return redirect("register")

        if not re.match(r"(?=.*[A-Z])", password1):
            messages.error(request, "Password must contain at least 1 uppercase letter.")
            return redirect("register")          

        if not re.match(r"(?=.*[@#$!])", password1):
            messages.error(request, "Password must contain at least special character: @, #, $ or !")
            return redirect("register")    
        
        myuser = User.objects.create_user(username, email, password1)
        myuser.first_name = forename
        myuser.last_name = surname
        myuser.is_staff = admin
        myuser.is_active = True
        myuser.save()
        messages.success(request, "Your account has been successfully created!")
        return redirect('signin')     

    return render(request, "asset_app/register.html")

def all_assets(request):
    if request.user.is_authenticated:
        forename = request.user.username
        if request.user.is_staff:
            assets = Asset.objects.all()
        else:
            assets = Asset.objects.filter(user=request.user)                     
        return render(request, "asset_app/all_assets.html",{"forename":forename,"assets":assets})        


def signin(request):
    if  request.method == "POST":
        username = request.POST['username']
        password1 = request.POST["password1"]
        user = authenticate(username=username, password=password1)

        # if user is not authenticated, none will be returned otherwise a not none object will be returned
        if user is not None:
            login(request, user)
            user.is_active = True
            user.save()
            return redirect('all_assets')       
        else:
            messages.error(request, "Invalid Credentials")
            return redirect('home')       
    return render(request, "asset_app/signin.html")

def add_asset(request):
    if request.user.is_authenticated:
        forename = request.user.username
        return render(request,"asset_app/add_asset.html", {"forename":forename})

def edit_asset(request, asset_id):
    if request.user.is_authenticated:
        user = request.user
        asset = Asset.objects.get(id=asset_id)
        form = AssetForm(request.POST or None, instance=asset)
        if form.is_valid():
            form.save()
            return redirect('all_assets')  
        return render(request, "asset_app/edit_asset.html", {"forename":user.username, "form":form})

def delete_asset(request, asset_id):
    if request.user.is_authenticated:
        if request.user.is_staff:
            asset = Asset.objects.get(id=asset_id)
            asset.delete()
            messages.success(request, "Your asset has been successfully deleted!")          
            return redirect('all_assets')        

def save_asset(request):
    if request.method == "POST":    
        if request.user.is_authenticated:
                user = request.user
                name = request.POST["name"]
                type = request.POST["type"]
                brand = request.POST["brand"]
                model_number = request.POST["model_number"]
                serial_number = request.POST["serial_number"]
                registration_date = request.POST["registration_date"]
                warranty = convert_to_bool(request.POST["warranty"])
                warranty_expiry = request.POST["warranty_expiry"]
                personal_device = convert_to_bool(request.POST["personal_device"])
                location = request.POST["location"]
                asset = Asset.objects.create(name=name, type=type, brand=brand,model_number=model_number,serial_number=serial_number,registration_date = registration_date, warranty=warranty, warranty_expiry = warranty_expiry, personal_device= personal_device,location= location,created_at=datetime.datetime.now(),user=user)
                messages.success(request, "Your asset has been successfully created!")                
                return render(request,"asset_app/add_asset.html", {"forename":user.username})
                
def signout(request):
    logout(request)
    messages.success(request, "Logged out successfully.")
    return redirect("home")


def convert_to_bool(value):
    if value == "true":
        return True
    else:
        return False

