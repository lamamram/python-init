# les imports sont calculés à partir du programme principal
# donc on utilise ici un "chemin absolu"
from utils.helpers.display import pretty_print
# from helpers.display import pretty_print
def ctrl_mean(values: str, delim: str=",", nb_sign: int=2, **kw):
    """
    calcule une moyenne à partir d'une ligne csv
    si possible
    return : float , error
    """
    values = values.split(delim)
    if "debug" in kw: print(pretty_print(values))
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