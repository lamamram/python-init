# %%
# requête HTTP
# 1/ URL
# http(s)://domain.name/path/to/resource?param=val&param2=val2#blabla

# proto.----|--domaine--|-----chemin-----|----query_string----|hash

# 2/ méthode ou verbe HTTP: mode d'accès à la ressource

# - GET: requête en lecture (avec query_string)
# - POST: requête en création (formulaires http, envoi de données)
# - PUT:  requête en modification complète (idem)
# - PATCH: requête en modification partielle(idem)
# - DELETE: requête en suppression

# 3/ si POST, PUT, ou PATCH: les données à envoyer

# 4/ des entête HTTP : métadonnées associée au client


# Réponse HTTP:

# 1/ le code de la réponse (Status Code)
#    - code 2XX : réponse OK
#    - code 3XX: réponse OK mais redirigée
#    - code 4xx: pb d'accès à la resource (404 not dound, 403 unauthorized)
#    - code 5xx: requête reçue mais pb sur le serveur

# 2/ le corps de la réponse
#     - en mode texte (html, xml, json, ...) avec un encodage
#     - en mode octets (images, fichiers téléchagés)

# 3/ entêtes de la réponse : métadonnées associées au serveur

# %%
from urllib.error import HTTPError
import requests

url = "https://gorest.co.in/public/v2/utsers"

try:
    r = requests.get(url)
    # code de retour
    if 200 <= r.status_code < 300:
        # analyse du type de corps de réponse
        if "json" in r.headers["content-type"]:
            print(r.json())
        elif "text" in r.headers["content-type"]:
            print(r.text.decode("utf8"))
        else:
            print(r.content)
    else: raise ValueError(f"code {r.status_code}: {r.text}") 
except (requests.ConnectionError, HTTPError, ValueError) as e:
    print(e, type(e))

# %%
from urllib.error import HTTPError
import requests
# pip install python-dotenv
from dotenv import load_dotenv
import os

# charge les variables du fichier .env à la racine
# commen variblaes d'environnement
load_dotenv()

URL = "https://gorest.co.in/public"
API_TOKEN = os.environ["API_TOKEN"]

class GoRestApi:
    def __init__(self, version="v2") -> None:
        self.__version = version
        self.__token = API_TOKEN

    
    def __call(self, endpoint, method, data={}, headers={}):
        url = f"{URL}/{self.__version}/{endpoint}"
        ret = {"valid": True, "response": None}
        if method.upper() in ("POST", "PUT", "DELETE"):
            headers["authorization"] = f"Bearer {self.__token}"
        try:
            call_fn = getattr(requests, method.lower())
            r = call_fn(url, data=data, headers=headers)
            # code de retour
            if 200 <= r.status_code < 300:
                # analyse du type de corps de réponse
                if "json" in r.headers["content-type"]:
                    ret["response"] = r.json()
                elif "text" in r.headers["content-type"]:
                    print(r.text.decode("utf8"))
                else:
                    print(r.content)
            else: raise ValueError(f"code {r.status_code}: {r.text}") 
        except (requests.ConnectionError, HTTPError, ValueError) as e:
            ret["valid"] = False
            ret["response"] = e
        return ret
    
    def get_users(self, page):
        return self.__call(f"users?page={page}", "GET")
    
    def get_all_users(self, page_start, page_end):
        ret = {"valid": True, "response": []}
        for i in range(page_start, page_end + 1):
            response = self.get_users(i)
            print(f"page {i} fetched")
            if response["valid"]: 
                ret["response"] += response["response"]
            else:
                ret["valid"] = False
                break
        return ret
    
    def create_user(self, user):
        return self.__call("users", "POST", data=user)
    
if __name__ == "__main__":
    api = GoRestApi()
    # print(api.get_users(2))
    # print(api.get_all_users(1, 10))
    print(api.create_user({
        "name": "matt LAMAM2",
        "email": "nawak2@example.com",
        "gender": "male",
        "status": "active"
    }))

# %%
class Truc:
    param = 1

t = Truc()
t.param
getattr(t, "param")
setattr(t, "machin", 2)
t.machin
# hasattr, delattr

# %%
