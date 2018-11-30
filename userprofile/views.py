from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.models import User


# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        return render(request, "userprofile/login.html", {"message":None})
    context = {
        "username" : request.user.username,
        "email" : request.user.email,
        "firstname" : request.user.first_name,
        "lastname" : request.user.last_name

    }
    return render(request, "userprofile/index.html", context)

def login_view(request):
    if request.method=="POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("order"))
        return render(request, "userprofile/login.html", {"message":"Invalid Credentials"})
    return HttpResponseRedirect(reverse("userprofile:index"))


def logout_view(request):
    if (request.method=="POST") and (request.user.is_authenticated):
        logout(request)
        #return render(request, "userprofile/logout.html", {"message":"Logout Successfully"})
        return HttpResponseRedirect(reverse("index"))
    return HttpResponseRedirect(reverse("userprofile:index"))

def new_user(request):
    if not request.user.is_authenticated:
        return render(request, "userprofile/new_user.html", {"message":"After Successfull Signup Redirected to login page!"})
    return HttpResponseRedirect(reverse("userprofile:index"))

def signup(request):
    if request.method=="POST":
        if request.user.is_authenticated:
            return render(request, "userprofile/login.html", {"message":None})
        username = request.POST["username"]
        password = request.POST["password"]
        email = request.POST["email"]
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        try:
            userexist = User.objects.get(username=username)
        except User.DoesNotExist:
            user = User.objects.create_user(username=username, password=password, email=email)
            user.last_name = lastname
            user.first_name = firstname
            user.save()
            login(request, user)
            return HttpResponseRedirect(reverse("userprofile:index"))
        return render(request, "userprofile/new_user.html", {"message":"Username already exist."})
    return HttpResponseRedirect(reverse("index"))


def editprofile(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("userprofile:index"))
    context = {
        "username" : request.user.username,
        "email" : request.user.email,
        "firstname" : request.user.first_name,
        "lastname" : request.user.last_name

    }
    return render(request, "userprofile/editprofile.html", context)

def doedit(request):
    if request.method=="POST":
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse("userprofile:index"))
        user = request.user
        username = request.POST["username"]
        password = request.POST["password"]
        email = request.POST["email"]
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        if password is not '':
            user.set_password('password')
            user.save()
        if email is not '':
            user.email = email
            user.save()
        if firstname is not '':
            user.first_name = firstname
            user.save()
        if lastname is not '':
            user.last_name = lastname
            user.save()
        if username is not '':
            try:
                userexist = User.objects.get(username=username)
            except User.DoesNotExist:   
                user.username = username
                user.save()
                return HttpResponseRedirect(reverse("userprofile:index"))
            return render(request, "userprofile/editprofile.html", {"message":"username already exist"})
        return HttpResponseRedirect(reverse("userprofile:index"))
    return HttpResponseRedirect(reverse("userprofile:index"))
        