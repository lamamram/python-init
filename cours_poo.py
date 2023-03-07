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
