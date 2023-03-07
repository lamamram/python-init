import re
# les imports se font toujours depuis le programme principal
from utils.helpers.exceptions import ValuesError
# même chose en relatif
# from .helpers.exceptions import ValuesError
# . et .. ne se manipule que si les packages sont reconnus (depuis l'extérieur)
FLOAT_PATTERN = "(-?[0-9])+(?:\.[0-9]*)?"

def calcul_moyenne(*values, float_pattern: float=FLOAT_PATTERN, precision: int=2, **opts):
    """
    *values: un ou n paramètres positionnels, disponibles
dans la foncition dans le tuple values
=> les params positionnels officiels doivent être à gauche
les paramètres nommés à droite
**opts: arguments nommés supplémentaires qui sont dispo
dans un dictionnaire
def is_float(item: str) -> bool:
    return re.match(FLOAT_PATTERN, item)
    """
    values = list(values)
    if not values: 
        raise ValueError("liste vide")

    # 1. filtrer sur ce qui est convertible
    # filtered = list(filter(is_float, values))
    filtered = list(filter(
        lambda val: re.match(float_pattern, val), 
        values
    ))
    issues = list(set(values) - set(filtered))
    if issues:
        if "debug" in opts and opts["debug"]:
            print(f"{issues}: non convertibles !!!")
        # lever une exception
        raise ValuesError(issues)
    # 2. appliquer la conversion sur les vecteur de données
    converted = list(map(float, filtered))
    moy = sum(converted) / len(converted)
    return round(moy, precision)

if __name__ == "__main__":
    print("coucou")