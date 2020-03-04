from __future__ import unicode_literals
from django.shortcuts import render, redirect
from login_app.models import User
from django.db import models
from .models import Moment, Comment
from time import strftime, strptime
from django.contrib import messages

def home(request):
    if "user_id" not in request.session:
        return redirect("/")
    context = {
        "existing_user" : User.objects.get(id=request.session["user_id"]),
        "all_moments" : Moment.objects.all().order_by("-created_at")

    }
    return render (request,"home.html", context)

def moment(request):
    if "user_id" not in request.session:
        return redirect("/")
    context = {
        "existing_user" : User.objects.get(id=request.session["user_id"])
    }
    return render(request, "moment.html", context)

def proc_moment(request):
    errors = Moment.objects.comment_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect ("/moment")
    else:
        print("made it to the moment")
        if request.method == "POST":
            Moment.objects.create(title=request.POST["title"], duration_min=request.POST["duration_min"], duration_sec=request.POST["duration_sec"], notes=request.POST["notes"], user=User.objects.get(id=request.session["user_id"]))
            print("MOMENT ADDED**********************************************************")
        return redirect ("/home")
    
    return redirect(request, "home.html")

def add_comment(request):
    errors = Comment.objects.c_validation(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect ("/home")
    else:
        if request.method == "POST":
            Comment.objects.create(comment=request.POST["comment"], user=User.objects.get(id=request.session["user_id"]), moment=Moment.objects.get(id=request.POST["moment_id"]))
            print("comment was addedTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT")
        return redirect("/home")

def delete_comment(request, id):
    if "user_id" not in request.session:
        return redirect("/")
    c = Comment.objects.get(id=id)
    c.delete()
    return redirect("/home")

def delete_moment(request,id):
    if "user_id" not in request.session:
        return redirect("/")
    m = Moment.objects.get(id=id)
    m.delete()
    return redirect("/home")