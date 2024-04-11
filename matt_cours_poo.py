# %%
# écriture CamelCase
class Account:

    # attributs de classe publics (on peut les retourner et les modifier directement)
    _id = None
    balance = 100.
    overdraft = False

    # quand on définit une méthode d'objet, il faut spécifier le premier paramètre
    # avec "self"
    def get_balance(self):
        return self.balance
    
    def set_balance(self, balance: float):
        self.balance = balance

# "appeler" la classe
# instanciation d'un objet acc à partir de la classe Account
# acc est une instance
acc = Account()

# retourner et affecter des attributs
acc._id, acc.balance
acc._id = 58483838383
acc._id

# utilisation des méthodes
# il y a toujours au moins un paramètre en moins dans l'appel des méthodes
# car self représente acc ici
acc.get_balance()
acc.set_balance(200.)

# différence entre l'attribut d'objet "acc.balance" ...
print(acc.get_balance())
# et l'attribut de classe
Account.balance

# %%
# L'ENCAPSULATION en POO

class Account:

    # attributs privés (préfixés par "__" et donc on ne peut plus retourner et modifier directement)
    __id = None
    __balance = 100.
    __overdraft = False

    def get_id(self):
        return self.__id
    
    def set_id(self, _id: int):
        self.__id = _id

    # quand on définit une méthode d'objet, il faut spécifier le premier paramètre
    # avec "self"
    def get_balance(self):
        return self.__balance
    
    def set_balance(self, balance: float):
        self.__balance = balance

acc = Account()
# acc.__id
## ce __id n'est pas le vrai !!!
acc.__id = 23
print(acc.__id)
## l'attribut __id ne peut être manipulé qu'avec les méthodes publiques
print(acc.get_id())


# %%

class Account:
    """
    classe de compte bancaire
    blabla
    """

    #------------------------attributs de classe -----------------------------#

    balance = 100.

    #------------------------méthodes magiques -----------------------------#

    # 1/ on veut initialiser les attributs des objets au moment de la création
    # la méthodes magique __init__ est best practice
    def __init__(self, _id, balance=100.) -> None:
        self.__id = _id
        self.__balance = balance
        self.__update_overdraft()
    
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

    #------------------------méthodes privée -----------------------------#

    # méthode privée donc inaccessible depuis l'extérieur
    # inaccesible uniquement avec les méthodes publiques
    def __update_balance(self, amount):
        self.__balance += amount
        self.__update_overdraft()

    
    def __update_overdraft(self):
        self.__overdraft = True if self.__balance < 0 else False

acc = Account(534543534)
acc.get_balance()

acc.deposit(100)
acc.get_balance()
acc.withdraw(300)
acc.get_balance()

# 
str(acc)
# print demande str() sur acc 
# et str(acc) demande acc.__str__()
print(acc)

acc2 = Account(233432423, 300)

# <=> acc.__add__(acc2)
acc + acc2




# %%
def fct():
    pass

fct.truc = 0
dir(fct)
fct = 3.14
fct
dir(fct)

fct = "hello"
dir(fct)

# tout est objet et classe en python!!!

class Truc:
    pass

t = Truc()
num = str(2)

type(t), type(num)
isinstance(num, str), isinstance(t, Truc)

# l'objet literal " " a une méthode public join
" ".join(["a", "b", "c"])

# %%

def mock_join(self: str, l: list[str]):
    _str = ""
    for elem in l:
        _str += elem + self
    _str.strip()

str.mock_join = mock_join

" ".mock_join(["a", "b", "c"])
    

# %%

from bank.account import BankAccount
from bank.client import Client


if __name__ == "__main__":
    cl = Client(132423423, "LAMAMRA", "matt", "13/02/1983")
    acc = BankAccount(34534544, cl, 500.)

    acc.get_client_name()
# %%
