from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from django.urls import reverse

from .models import SearchCount
from .riotapi import *
from pprint import pprint

'''

TODOs

Introduce error handling process

'''


def index(request):
    return render(request, "smtsgg/index.html")

def search(request):
    nickname, tag = request.POST.get("playerName").split("#")
    tag = "KR1" if tag == "" else tag
    try:
        puuid = get_puuid(nickname, tag)
        # record_list = SearchCount.objects.filter(puuid=puuid)
        # if len(record_list) == 0:
        #     new_record = SearchCount(puuid=puuid, gamename=nickname, tagline=tag)
        #     new_record.save()
        # else:
        #     record = record_list[0]
        #     record.count += 1
        #     record.save()

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
    rank_info = get_rank_info(puuid)

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
        context["match_list"].append(get_match_for_single_player(mid, puuid))

    context["mastery_list"] = get_champion_mastery(puuid)

    return render(request, "smtsgg/detail.html", context=context)

def match_detail(request, match_id):
    match_infos = get_match_detail(match_id)
    context = {
        "game_info": match_infos["game_info"],
        "winning_team": match_infos["winning_team"],
        "losing_team": match_infos["losing_team"],
    }
    return render(request, "smtsgg/match_detail.html", context=context)