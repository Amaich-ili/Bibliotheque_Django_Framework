from multiprocessing import context
from urllib import request
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
# from django. contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import *
from .forms import *
from . import dico


def index(response):
    return render(response, 'main/bas.html', {})

def livre(response):
    livre = Liste_livre.objects.all()
    context = {'livre' : livre}
    return render(response, "main/livre.html", context)

def livre_policier(response):
    ls = Categories.objects.get(id=1)
    context = {'ls' : ls}
    return render(response, "main/policier.html", context)

def livre_science(response):
    ls = Categories.objects.get(id=2)
    context = {'ls' : ls}
    return render(response, "main/science.html", context)

def livre_cuisine(response):
    ls = Categories.objects.get(id=3)
    context = {'ls' : ls}
    return render(response, "main/cuisine.html", context)

def livre_enfant(response):
    ls = Categories.objects.get(id=4)
    context = {'ls' : ls}
    return render(response, "main/enfant.html", context)

def jeu(response):
    context = {}
    return render(response, "main/jeu.html", context)

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
    context = {}
    return render(request, 'main/login.html', context)

def logout_user(request):
    logout(request)
    return redirect('index')

def jeu_py(request):
    return render(request, 'main/jeu_py.html', {})


# @csrf_exempt
# def jeu_py(request):
#     if request.method == 'POST':
#         return JsonResponse({"data" : data})

# @csrf_exempt
# def jeu_py(request):
#     if request.method == 'POST':
#         data = json.loads(request.body)
#     return JsonResponse({"data": "data"})
