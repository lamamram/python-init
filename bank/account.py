# %%
from bank.client import Client

class BankAccount:
    """
    classe de compte bancaire
    blabla
    """

    # ------------------------attributs de classe -----------------------------#

    balance = 100.

    # ------------------------méthodes magiques -----------------------------#

    # 1/ on veut initialiser les attributs des objets au moment de la création
    # la méthodes magique __init__ est best practice
    # 2/ ici on injecte un objet de type Client => on ne connaît pas son code
    def __init__(self, _id: int, client: Client, balance: float=100.) -> None:
        self.__id = _id
        self.__balance = balance
        self.__update_overdraft()
        self.__client = client

    def __str__(self):
        return f"account id: {self.__id}, overfraft: {self.__overdraft}"

    def __add__(self, other) -> float:
        return self.__balance + other.get_balance()

    #------------------------méthodes publiques -----------------------------#

    def get_balance(self):
        return self.__balance

    def deposit(self, amount: float):
        """
        dépôt positif
        """
        if amount > 0:
            self.__update_balance(amount)

    def withdraw(self, amount: float):
        """
        retrait positif
        """
        if amount > 0 and amount:
            self.__update_balance(-amount)
    
    # pour piloter l'attribut "client" on a besoin uniquement de ces métodes publiques
    # le nom, les paramètres et les valeurs de retour
    # => on a un couplage faible entre BankAccount et Client 
    # => l'injection de dépendance
    def get_client_name(self):
        return self.__client.get_full_name(mode="nawak")

    #------------------------méthodes privée -----------------------------#

    # méthode privée donc inaccessible depuis l'extérieur
    # inaccesible uniquement avec les méthodes publiques
    def __update_balance(self, amount):
        self.__balance += amount
        self.__update_overdraft()


    def __update_overdraft(self):
        self.__overdraft = True if self.__balance < 0 else False
# %%
