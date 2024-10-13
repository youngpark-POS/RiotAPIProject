from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from django.urls import reverse

from .riotapi import get_puuid, get_match_ids, get_single_match, get_champion_mastery
from pprint import pprint

# Create your views here.

def index(request):
    return render(request, "smtsgg/index.html")

def search(request):
    nickname, tag = request.POST["playerName"].split("#")

    puuid = get_puuid(nickname, tag)
    # get user info from API query

    if puuid is None:
        raise Http404("Summoner name not found, or just API key expiration")
    else:
        return redirect("smtsgg:detail", "#".join([nickname, tag]))

def detail(request, nickname_and_tag):
    nickname, tag = nickname_and_tag.split("#")

    puuid = get_puuid(nickname, tag)
    match_ids = get_match_ids(puuid)

    context = {
        "nickname_and_tag": nickname_and_tag,
        "current_rank" : "",
        "current_LP" : "",
        "match_list": [],
        "mastery_list": [],
    }

    for mid in match_ids:
        context["match_list"].append(get_single_match(mid, puuid))

    context["mastery_list"] = get_champion_mastery(puuid)

    return render(request, "smtsgg/detail.html", context=context)