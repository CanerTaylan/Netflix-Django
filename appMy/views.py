from django.shortcuts import render
from appUser.views import Profil
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth.decorators import login_required



# Create your views here.


def index(request):
    context = {
    }
    return render(request, 'index.html', context)

@login_required
def netflixPage(request, id):

    profil = Profil.objects.get(id=id)
    filmler = Films.objects.all()
    diziler = Series.objects.all()

    context = {
        "profil": profil,
        "filmler": filmler,
        "diziler": diziler,
    }
    return render(request, 'netflix.html', context)

@login_required
def Diziler(request, id):

    profil = Profil.objects.get(id=id)
    diziler = Series.objects.all()

    context = {
        "profil": profil,
        "diziler": diziler,
    }
    return render(request, 'dizi.html', context)

@login_required
def Filmler(request, id):

    profil = Profil.objects.get(id=id)
    filmler = Films.objects.all()

    context = {
        "profil": profil,
        "filmler": filmler,
    }
    return render(request, 'film.html', context)
