import requests, json
from urllib import parse  # for utf-8 encoding

with open("data.json") as f:
    json_object = json.load(f)

encodeName = json_object["user-name"]
tagLine = json_object["tagline"]
header_content = json_object["header-content"]
api_base_url = "https://kr.api.riotgames.com"

player_id_query_url = "/".join([api_base_url, f"riot/account/v1/accounts/by-riot-id/{encodeName}/{tagLine}"])

player_id = requests.get(player_id_query_url, headers=header_content).json()
if json_object["puuid"] == "":
    json_object["puuid"] = player_id["puuid"]
    with open("data.json", "w") as f:
        json.dump(json_object, f, indent="\t")

print(player_id)
