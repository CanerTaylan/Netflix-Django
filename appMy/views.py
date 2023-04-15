from django.shortcuts import render
from appUser.views import Profil

# Create your views here.


def index(request):
    context = {
    }
    return render(request, 'index.html', context)


def netflixPage(request, id):

    profil = Profil.objects.get(id=id)
    context = {
        "profil":profil,

    }
    return render(request, 'netflix.html', context)
