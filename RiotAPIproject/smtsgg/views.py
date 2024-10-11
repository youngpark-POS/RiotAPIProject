from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from django.urls import reverse

from . import riotapi
# Create your views here.

def index(request):
    return render(request, "smtsgg/index.html")

def search(request):
    nickname, tag = request.POST["playerName"].split("#")

    puuid = riotapi.get_puuid(nickname, tag)
    # get user info from API query

    if puuid is None:
        raise Http404("Summoner name not found, or just API key expiration")
    else:
        return HttpResponseRedirect(reverse("smtsgg:detail", args=("#".join((nickname, tag)),)))

def detail(request, nickname):
    name, tag = nickname.split("#")
    return HttpResponse("detail page, Not built yet")