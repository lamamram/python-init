"""
module de fonctions arithmétiques
liste:
- ctrl_mean
"""

SIGN_NUMBERS = 2

def ctrl_mean(values: str, delim: str=",", nb_sign: int=SIGN_NUMBERS, **kw):
    """
    calcule une moyenne à partir d'une ligne csv
    si possible
    return : float , error
    """
    values = values.split(delim)
    numbers = []
    for value in values:
        value = value.strip()
        if value.isnumeric() or (value[0] == "-" and value[1:].isnumeric()):
            numbers.append(int(value))
        else:
            return None, f"bad value: {value}"
    else:
        return round(sum(numbers)/len(numbers), nb_sign), None


if __name__ == "__main__":
    # faire des tests
    print("exécuté en tant que programme principal !!!")