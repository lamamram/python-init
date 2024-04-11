# %%
class Client:
    """
    classe de client de compte bancaire
    interface publique:
    - get_full_name
    - reminder_joint_birth_date
    """

    def __init__(self, _id: int, last_name: str, first_name: str, joint_date: str) -> None:
        self.__id = _id
        self.__last_name = last_name
        self.__first_name = first_name
        self.__joint_date = joint_date
    

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
# %%
