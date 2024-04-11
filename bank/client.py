# %%
from datetime import datetime, timedelta
import re

class Client:
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
        self.__last_name = last_name
        self.__first_name = first_name

        for fmts, dt_fmt in self.__pattern_formats.items():
            if re.match(fmts, joint_date):
                    f = dt_fmt
                    break
        else:
            # on va faire planter nous même le code
            raise ValueError(f"{joint_date}: bad format")

        self.__joint_date =  datetime.strptime(joint_date, f)
    

    def get_full_name(self, **params):
        """
        retourne le nom complet du client
        """
        if "mode" in params:
            pass
        return f"{self.__first_name.capitalize()} {self.__last_name.upper()}"

    def reminder_joint_birth_date(self) -> bool:
        """
        retourne vrai si on est la date anniversaire
        """
        dt = datetime.now()
        return self.__joint_date.month == dt.month and self.__joint_date.day == dt.day
# %%
