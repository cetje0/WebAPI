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

def D_D_ALLE_alignments():
     try:
          url = f"https://www.dnd5eapi.co/api/alignments/"
          response_json = requests.get(url).json()
          return response_json["results"]
     except requests.exceptions.JSONDecodeError:
          return False

def D_D_alignments_info(alignment_keuze: str) -> dict:
     try:
          url = f"https://www.dnd5eapi.co/api/alignments/{alignment_keuze}"
          response_json = requests.get(url).json()
          return response_json
     except requests.exceptions.JSONDecodeError:
          return False
     
def D_D_language():
     try:
          url = f"https://www.dnd5eapi.co/api/languages/"
          response_json = requests.get(url).json()
          return response_json["results"]
     except requests.exceptions.JSONDecodeError:
          return False

def D_D_language_info(language_keuze: str) -> dict:
     try:
          url = f"https://www.dnd5eapi.co/api/languages/{language_keuze}"
          response_json = requests.get(url).json()
          return response_json
     except requests.exceptions.JSONDecodeError:
          return False