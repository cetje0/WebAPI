import requests, json

url = "https://www.dnd5eapi.co/api/ability-scores/"
response = requests.get(url)
response_json = response.json()

with open(r"project\test\ability-scores.json", "w") as fp:
    json.dump(response_json, fp)
    print("Data gedumpt!")
