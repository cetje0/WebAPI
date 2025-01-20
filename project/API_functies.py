import requests

def D_D_abilitys(search: str) -> dict:
        " Geef het eerste drankje gevonden op basis van de 'search' "
        url= f"https://www.dnd5eapi.co/api/ability-scores/{search}"
        response_json = requests.get(url).json()


        if response_json == {"name": None}:
          return False
        return response_json["name"][0]

