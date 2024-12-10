from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from django.urls import reverse

from .riotapi import *
from pprint import pprint

'''

TODOs 

Introduce error handling process

'''


def index(request):
    return render(request, "smtsgg/index.html")

def search(request):
    nickname, tag = request.GET.get("playerName").split("#")
    try:
        puuid = get_puuid(nickname, tag)
        return redirect("smtsgg:detail", "#".join([nickname, tag]))
    # get user info from API query
    except KeyError:
        raise Http404("Summoner name not found")
    except Exception:
        raise Http404("Unknown error")

def detail(request, nickname_and_tag):
    nickname, tag = nickname_and_tag.split("#")

    puuid = get_puuid(nickname, tag)
    match_ids = get_match_ids(puuid)
    summid = get_summoner_id_encrypted(puuid)
    rank_info = get_rank_info(summid)

    context = {
        "nickname_and_tag": nickname_and_tag,
        "current_rank_solo" : " ".join([rank_info["solo"]["tier"], rank_info["solo"]["rank"]]),
        "current_LP_solo" : str(rank_info["solo"]["leaguePoints"]) + ("" if rank_info["solo"]["tier"] == "Unranked" else "LP"),
        "current_rank_flex" : " ".join([rank_info["flex"]["tier"], rank_info["flex"]["rank"]]),
        "current_LP_flex" : str(rank_info["flex"]["leaguePoints"]) + ("" if rank_info["flex"]["tier"] == "Unranked" else "LP"),
        "match_list": [],
        "mastery_list": [],
    }

    for mid in match_ids:
        context["match_list"].append(get_single_match(mid, puuid))

    context["mastery_list"] = get_champion_mastery(puuid)

    return render(request, "smtsgg/detail.html", context=context)