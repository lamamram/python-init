# %%
from utils.cleaner import Cleaner
from utils.misc import get_occurences

class Counter:

    # sans couplage: counter ne connait pas cleaner
    # le texte doit déjà être nettoyé sinon analyse fauss
    # def __init__(self, text: str) -> None:
    #     self.__text = text

    # injection de dépendance
    # la classe Counter utilise la classe Cleaner
    # avec un couplage le plus faible possible
    # => n'a besoin de connaitre que la méthode publique clean
    def __init__(self, cleaner: Cleaner) -> None:
        self.__text = cleaner.clean()

    # couplage plus fort:
    # Counter doit connaître l'interface
    # et les attributs (complique la maintenabilité)
    # def __init__(self, text, punc, min_length):
    #     self.__text = Cleaner(text, punc, min_length).clean()
    
    def get_occurences(self, limit: int=5):
        occ = get_occurences(self.__text)
        occ = sorted(
            occ.items(),
            # fonction qui retourne une valeur
            # sur laquelle on trie 
            key=lambda tup: tup[1],
            reverse=True
        )
        return dict(occ[:limit])