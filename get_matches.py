import os

import requests, json
import pprint
from urllib import parse  # for utf-8 encoding

pp = pprint.PrettyPrinter(indent=4)

api_base_url = "https://asia.api.riotgames.com"

with open("data.json") as f:
    json_object = json.load(f)

puuid = json_object["puuid"]
header_content = json_object["header-content"]

detail_url = f"lol/match/v5/matches/by-puuid/{puuid}/ids"

url = "/".join([api_base_url, detail_url])
print(url)

match_ids = requests.get(url, headers=header_content).json()
pp.pprint(match_ids)
