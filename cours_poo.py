# %%
# CamelCase: les mots sont séparés par des majuscules
class Account:
    """
    classe de gestion de compte en banque
    """
    # attribut de classe publique
    balance = 100.

    # méthode publique
    # le premier paramètre de toute méthode de classe (hors static)
    # représente une instance de la classe, et est nommé par convention self
    def deposit(self, amount: float):
        """
        dépôt: ajout d'une somme au compte
        """
        # on accède aux attributs à travers self 
        self.balance += amount

acc = Account()
acc.balance
# quand on appelle une méthode, on ne tient pas compte
# du premier paramètre self de la def, car acc est self
acc.deposit(200)
acc.balance

dir(Account)
# %%
class Account:
    # préfixer un attribut (ou une méthode) par "__"
    # le rend inaccessible depuis l'extérieur
    __balance = 100.

    # méthode privée: inaccessible depuis l'extérieur
    def __set_balance(self, amount: float):
        self.__balance += amount

    # méthode publique: interface entre le contexte
    # externe et les éléments privés
    # sécurité, contrôle
    def deposit(self, amount: float):
        if amount > 0:
            self.__set_balance(amount)
    
    def withdraw(self, amount: float):
        if amount > 0:
            self.__set_balance(-amount)
    
    def get_balance(self):
        return self.__balance

acc = Account()
# l'accès aux méthodes et aux attributs est publique
# par défaut
# => utilisable par l'objet instancié, depuis l'extérieur de
#la classe
acc.deposit(200)
# acc.__balance
# encapsulation: on accède aux attributs privés depuis l'instance
# qu'à travers les méthodes publiques
acc.withdraw(100)
acc.get_balance()
# acc.__set_balance(200)
# %%
