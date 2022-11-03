from multiprocessing import context
from urllib import request
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django. contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .models import *
from .forms import *


def index(response):
    return render(response, 'main/bas.html', {})

def livre(response):
    livre = Liste_livre.objects.all()
    context = {'livre' : livre}
    return render(response, "main/livre.html", context)

def register_page(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('first_name')
            messages.success(request, 'Votre compte '+ user + ' a été créé avec succès')
            return redirect('login')
    context = {'form':form}
    return render(request, 'main/register.html', context)

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get("identifiant")
        password = request.POST.get("password")
        user = authenticate(request, username = username, password = password) 
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request,"Invalide identifiant ou mot de passe")
            # return redirect('login')
    context = {}
    return render(request, 'main/login.html', context)

def logout_user(request):
    logout(request)
    return redirect('index')