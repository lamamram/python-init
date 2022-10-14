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
