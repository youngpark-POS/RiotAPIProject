import os

import requests, json
from urllib import parse  # for utf-8 encoding

api_base_url = "https://kr.api.riotgames.com"

with open("data.json") as f:
    json_object = json.load(f)

puuid = json_object["puuid"]
header_content = json_object["header-content"]


url = "/".join([api_base_url, f"lol/champion-mastery/v4/champion-masteries/by-puuid/{puuid}"])

mastery_info = requests.get(url, headers=header_content).json()
print(json.dumps(mastery_info[0], indent=4))