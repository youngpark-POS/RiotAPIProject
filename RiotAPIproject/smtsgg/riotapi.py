import requests
import json
from . import config as conf

from pprint import pprint

API_BASE_URL_KR = "https://kr.api.riotgames.com"
API_BASE_URL_ASIA = "https://asia.api.riotgames.com"

def get_puuid(userName, tagLine):
    header_content = conf.header_content

    query_url = "/".join([API_BASE_URL_ASIA, f"riot/account/v1/accounts/by-riot-id/{userName}/{tagLine}"])

    response = requests.get(query_url, headers=header_content)

    if response.status_code == 200:
        return response.json()["puuid"]
    else:
        return None
    
def get_summoner_info(puuid):
    header_content = conf.header_content

    query_url = "/".join([API_BASE_URL_KR, f"lol/summoner/v4/summoners/by-puuid/{puuid}"])

    response = requests.get(query_url, headers=header_content)

    if response.status_code == 200:
        return response.json()
    else:
        return None

    
def get_matches(puuid):
    header_content = conf.header_content

    query_url = "/".join([API_BASE_URL_ASIA, f"lol/match/v5/matches/by-puuid/{puuid}/ids"])

    response = requests.get(query_url, headers=header_content)

    if response.status_code == 200:
        return response.json()
    else:
        return None

    # return match id list

def get_champion_mastery(puuid):
    header_content = conf.header_content

    query_url = "/".join([API_BASE_URL_KR, f"lol/champion-mastery/v4/champion-masteries/by-puuid/{puuid}"])

    response = requests.get(query_url, headers=header_content)

    if response.status_code == 200:
        return response.json()
    else:
        return None