# %%
from utils.cleaner import Cleaner
from utils.misc import count_occurences

class Counter:

    # injection de dépendance
    # la classe Counter utilise la classe Cleaner
    # avec un couplage le plus faible possible
    # => n'a besoin de connaitre que la méthode publique clean
    def __init__(self, cleaner: Cleaner) -> None:
        self.__text = cleaner.clean()
    
    def get_occurences(self, limit: int=5):
        occ = count_occurences(self.__text)
        occ = sorted(
            occ.items(),
            # fonction qui retourne une valeur
            # sur laquelle on trie 
            key=lambda tup: tup[1],
            reverse=True
        )
        return dict(occ[:limit])