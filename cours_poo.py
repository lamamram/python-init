# %%
"""
docstring module
"""
class Account:
    """
    classe Account
    """
    # attributs de classe

    # dans python, le premier argument de toute 
    # méthodes est toujours l'instance, ici self
    # __init__: initialiseur: permet de renseigner
    # des attributs à l'instanciation
    def __init__(self, _id, balance=100.) -> None:
        # attributs d'instance
        # attribut privé, préfixé par "__"
        self.__id = _id
        # attribut public
        self.balance = balance

if __name__ == "__main__":
    acc = Account(1233434)
    print(acc.balance)
    # print(acc.__id)
    #pas de vrai encapsulation
    print(acc._Account__id)
# %%
class Account:
    
    def __init__(self, _id, balance=100.) -> None:
        self.__id = _id
        self.__balance = balance
    
    # méthodes publiques
    def get_balance(self):
        return self.__balance
    
    def withdraw(self, amount: float):
        if amount > 0:
            self.__update_balance(-amount)

    def deposit(self, amount: float):
        if amount > 0:
            self.__update_balance(amount)

    # méthode privée
    def __update_balance(self, amount: float):
        self.__balance += amount

if __name__ == "__main__":
    # en python on ne répète le premier argument à l'appel => self
    # puisque c'est l'instance acc qui appelle
    acc = Account(1233434)
    acc.deposit(300)
    acc.withdraw(100)
    print(acc.get_balance())
# %%
from typing import Any
# méthodes magiques
class Account:
    
    def __init__(self, _id, balance=100.) -> None:
        self.__id = _id
        self.__balance = balance
    
    def __str__(self) -> str:
        return f"id: {self.__id}, balance: {self.__balance}"
    
    def __add__(self, alt: Any):
        if isinstance(alt, Account):
        # if issubclass()...
            return self.__balance + alt._Account__balance
        elif isinstance(alt, float):
            return self.__balance + alt

acc = Account(1234)
acc2 =  Account(1234, 200.)
print(acc)
# polymorphisme
print(acc + acc2)
print(acc + 50.)
# %%
# itéranle

class IterExp:
    # fixer la condition limite
    def __init__(self, val=2, limit=10) -> None:
        self.__val = val
        self.__limit = limit

    # (re)initialiser le compteur
    # transofmrer un itérable en itérateur
    def __iter__(self):
        self.__cpt = 1
        return self
    
    # teste la condition limite
    # calcule la valeur de sortie
    # met à jour le compteur
    # ou interrompt l'itération
    def __next__(self):
        if self.__cpt < self.__limit:
            ret = self.__val ** self.__cpt
            self.__cpt += 1
            return ret
        else:
            raise StopIteration

# instanciation itérable
p2 = IterExp()
# transformation en itérateur
it = iter(p2)
# exécution pas à pas
for _ in range(1, 10):
    print(next(it))

for p in p2:
    print(p)
# %%

# générateur en python => itérable à partir d'une fonction
# fonciton génératrice
def iter_exp(val=2, limit=10):
    for i in range(1, limit):
        # yield interrompt l'exécution de la fonction
        # jusqu'au prochain appel à next()
        yield val ** i

# objet générateur
# g = iter_exp()

for p in iter_exp():
    print(p)

list(iter_exp())
# %%
from sys import getsizeof
r = range(1000000)
l = list(range(1000000))
getsizeof(r), getsizeof(l)
# %%
