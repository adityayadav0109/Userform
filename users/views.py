import email
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from . forms import *
# import pandas as pd
# Create your views here.
def home(request):
    return render(request, "users/home.html")

def register(request):

    form = UserForm()
    context = {"form": form}

    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "users/login.html")

    return render(request, "users/register.html", context)


def login(request):
    form = LoginForm()
    context = {"form": form}
    # return render(request, "users/login.html", context )

    if request.method == 'POST':

        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email = email, password = password)
            if user is not None:
                login(request, user)

                return redirect('user_data')


            else:
                form = LoginForm()
                context = {"form": form}
                return render(request, "users/login.html", context )



    return render(request, "users/login.html", context)


def user_data(request):
    user  = request.user
    context = {'user':user}
    return render(request, "users/user_data.html", context)