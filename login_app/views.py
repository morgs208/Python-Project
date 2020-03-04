from __future__ import unicode_literals
from django.shortcuts import render, redirect
from .models import User
from time import strftime, strptime
from django.contrib import messages
import bcrypt, re

def login(request):
    return render (request, "login.html")

def process_registration(request):
    print("***********It has made it to the process POINT")
    if request.method != "POST":
        return redirect("/")
    errors = User.objects.reg_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/")
    else:
        password = request.POST["reg_password"]
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        new_user = User.objects.create(first_name=request.POST["reg_first_name"], last_name=request.POST["reg_last_name"], email=request.POST["reg_email"], password=pw_hash)
        print("New User:", new_user.id)
        print("THIS USER HAS BEEN MADE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print(pw_hash)
        request.session['user_id'] = new_user.id
        return redirect("/success")
        

def success(request):
    if "user_id" not in request.session:
        return redirect("/")
    context = {
        "the_user" : User.objects.get(id=request.session['user_id'])
    }
    return render (request, "success.html", context)


def process_login(request):
    print("made it to this login spot")
    if request.method != "POST":
        return redirect("/")
    validate = User.objects.login_validator(request.POST)
    if len(validate["errors"]) > 0:
        for key, value in validate["errors"].items():
            messages.error(request, value)
        return redirect("/")
    else:
        request.session["user_id"] = validate["user"].id
        return redirect("/home")

def logout(request):
    request.session.clear()
    return redirect ("/")
