import os

import requests, json
from urllib import parse  # for utf-8 encoding

api_base_url = "https://kr.api.riotgames.com"

with open("data.json") as f:
    json_object = json.load(f)

puuid = json_object["puuid"]
header_content = json_object["header-content"]


url = "/".join([api_base_url, f"lol/summoner/v4/summoners/by-puuid/{puuid}"])
print(url)

summoner_info = requests.get(url, headers=header_content).json()

if "user-id-encrypted" not in json_object:
    json_object["user-id-encrypted"] = summoner_info["id"]
if "account-id-encrypted" not in json_object:
    json_object["account-id-encrypted"] = summoner_info["accountId"]
    
with open("data.json", "w") as f:
    json.dump(json_object, f, indent="\t")

print(summoner_info)