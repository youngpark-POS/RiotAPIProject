import os
import requests
import json
from datetime import datetime as dt
from . import config as conf

from pprint import pprint

API_BASE_URL_KR = "https://kr.api.riotgames.com"
API_BASE_URL_ASIA = "https://asia.api.riotgames.com"

def get_puuid(userName, tagLine):

    query_url = "/".join([API_BASE_URL_ASIA, f"riot/account/v1/accounts/by-riot-id/{userName}/{tagLine}"])

    response = requests.get(query_url, headers=conf.header_content)

    if response.status_code == 200:
        return response.json()["puuid"]
    else:
        return None
    
def get_summoner_id_encrypted(puuid):
    query_url = "/".join([API_BASE_URL_KR, f"lol/summoner/v4/summoners/by-puuid/{puuid}"])

    response = requests.get(query_url, headers=conf.header_content)

    if response.status_code == 200:
        return response.json()["id"]
    else:
        return None

    
def get_match_ids(puuid):

    query_url = "/".join([API_BASE_URL_ASIA, f"lol/match/v5/matches/by-puuid/{puuid}/ids"])

    response = requests.get(query_url, headers=conf.header_content)

    if response.status_code == 200:
        return response.json()
    else:
        return None

#  returns match information given match ID and puuid
def get_single_match(match_id, puuid):

    query_url = "/".join([API_BASE_URL_ASIA, f"lol/match/v5/matches/{match_id}"])

    response = requests.get(query_url, headers=conf.header_content)

    if response.status_code == 200:
        minfo = response.json()
        for p in minfo["info"]["participants"]:
            if p["puuid"] == puuid:
                target_player = p
                break
        infos_used = {
            "game_duration": minfo["info"]["gameDuration"],
            "game_endtime": dt.fromtimestamp(minfo["info"]["gameEndTimestamp"] / 1000).strftime("%Y/%m/%d %H:%M:%S"),
            "mapId": minfo["info"]["mapId"],
            "gameMode": minfo["info"]["gameMode"],
            "kills": target_player["kills"],
            "assists": target_player["assists"],
            "deaths": target_player["deaths"],
            "win": target_player["win"],
            "champion": target_player["championName"],
        }
        return infos_used
    else:
        return None

#  returns the list of top 5 champion mastery
def get_champion_mastery(puuid):

    query_url = "/".join([API_BASE_URL_KR, f"lol/champion-mastery/v4/champion-masteries/by-puuid/{puuid}/top?count=5"])

    response = requests.get(query_url, headers=conf.header_content)

    if response.status_code == 200:
        infos_used = []
        with open(os.path.join(os.path.dirname(__file__), "static", "champ_id2name.json"), "r", encoding="utf-8") as f:
            id2name_dict = json.load(f)
            for mst in response.json():
                single_mastery = {
                    "championName": id2name_dict[str(mst["championId"])],
                    "championPoints": mst["championPoints"],
                    "championLevel": mst["championLevel"],
                }
                infos_used.append(single_mastery)
        return infos_used
    else:
        return None
    
def get_rank_info(summid):
    query_url = "/".join([API_BASE_URL_KR, f"lol/league/v4/entries/by-summoner/{summid}"])

    response = requests.get(query_url, headers=conf.header_content)

    if response.status_code == 200:
        target_player = None
        for p in response.json():
            if p["summonerId"] == summid:
                target_player = p
                break
        if target_player is None:
            infos = {
                "tier": "Unranked",
                "rank": "",
                "leaguePoints": ""
            }
        else:
            infos = {
                "tier": target_player["tier"],
                "rank": target_player["rank"],
                "leaguePoints": target_player["leaguePoints"]
            }
        return infos
    else:
        return None