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

    __formats = {"-": "%Y-%m-%d", "/": "%Y/%m/%d"} 
    # () => crée des groupes pour faire des quantificateur
    __pattern_format = "[0-9]{4}[-/]([0-9]{2}[-/]?){2}"

    def __init__(self, _id: int, last_name: str, first_name: str, joint_date: str) -> None:
        self.__id = _id
        self.__last_name = last_name
        self.__first_name = first_name

        f = None
        if re.match(self.__pattern_format, joint_date):
            for k in self.__formats:
                if k in joint_date:
                    f = self.__formats.get(k, None)
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
