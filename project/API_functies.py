import requests

def D_D_abilitys(ability_keuze: str) -> dict:
        try :
          url= f"https://www.dnd5eapi.co/api/ability-scores/{ability_keuze}"
          response_json = requests.get(url).json()
          return response_json['skills']
        except requests.exceptions.JSONDecodeError:
              return False
        
def D_D_abilitys_info(ability_keuze: str) -> dict:
        try:
          url= f"https://www.dnd5eapi.co/api/ability-scores/{ability_keuze}"
          response_json = requests.get(url).json()
          return response_json['desc']
        except requests.exceptions.JSONDecodeError:
             return False