# %%
from datetime import datetime, timedelta
import re

# on a déporté la gestion des attributs last_name et first_name 
# car ils seront utiles pour d'autres classes
class Person:
    def __init__(self, last_name: str, first_name: str) -> None:
        self.__last_name = last_name
        self.__first_name = first_name
    
    # dans le cas d'un héritage, les objets enfants peuvent utiliser les méthodes publiques
    # de la classe parent: usage générique 
    def get_full_name(self, **params):
        """
        retourne le nom complet de la personne
        """
        if "mode" in params:
            pass
        return f"{self.__first_name.capitalize()} {self.__last_name.upper()}"

class ParentB:
    def __init__(self) -> None:
        pass
    def bidon_fct(p):
        pass
class Manager(Person):
    pass

# Client veut utiliser ces attributs du manière héritée
# on dit que Client est une Person
class Client(Person, ParentB):
    """
    classe de client de compte bancaire
    interface publique:
    - get_full_name
    - reminder_joint_birth_date
    """

    __pattern_formats = {
        "[0-9]{4}-[0-9]{2}-[0-9]{2}": "%Y-%m-%d", 
        "[0-9]{2}/[0-9]{2}/[0-9]{4}": "%d/%m/%Y"
    } 
    # () => crée des groupes pour faire des quantificateur
    # "[0-9]{4}[-/]([0-9]{2}[-/]?){2}"

    def __init__(self, _id: int, last_name: str, first_name: str, joint_date: str) -> None:
        self.__id = _id
        # la surcharge de la méthode de __init__
        ## REM: en cas d'héritage multiple on a un algorithme: MRO ( Method Resolution Order)
        # quand on a un conflit de nom de classe parent, on prend le premier a priori
        # super exécute la méthode __init__ de Person sur l'objet client
        super().__init__(last_name, first_name)
        # si on veut un autre exemplaire, on doit utiliser la classe voulue
        # en exécutant une méthode de classe, qui va demander l'objet en premier paramètre
        ParentB.__init__(self)

        for fmts, dt_fmt in self.__pattern_formats.items():
            if re.match(fmts, joint_date):
                    self.__joint_date =  datetime.strptime(joint_date, dt_fmt)
                    break
        else:
            # on va faire planter nous même le code
            raise ValueError(f"{joint_date}: bad format")

    ## usage spécifique de la classe enfant
    def reminder_joint_birth_date(self) -> bool:
        """
        retourne vrai si on est la date anniversaire
        """
        dt = datetime.now()
        return self.__joint_date.month == dt.month and self.__joint_date.day == dt.day
# %%
