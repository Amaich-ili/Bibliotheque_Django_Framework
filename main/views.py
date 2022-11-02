from django.shortcuts import render
from .models import *


def index(response):
    return render(response, 'main/bas.html', {})

def livre(response):
    livre = Liste_livre.objects.all()
    context = {'livre' : livre}
    return render(response, "main/livre.html", context)