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
print(acc.balance)

dir(Account)
Account.balance
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
# implémentation incomplète
# acc._Account__balance

# %%
# en python, tout est objet !!!
class Truc:
    pass

t = Truc()
dico = dict(k="v")
print(type(t), type(dico))
print(isinstance(t, Truc), isinstance(dico, dict))

chaine = str("bonjour")
chaine.upper()
# %%
# comportements codés sur les objets custom
class Account:
    # initialiseur != constructeur
    def __init__(self, balance=100.) -> None:
        # attributs d'objet
        self.balance = balance
    
    def __str__(self) -> str:
        return f"solde: {self.balance}"
    
    def __add__(self, account):
        return self.balance + account.balance
    
    def __lt__(self, account):
        return self.balance < account.balance

# __init__ permet l'instanciation avec des paramètres
acc = Account(balance=200)
acc.balance
# __str__ permet d'afficher ou de convertir l'objet en chaine
print(acc)
str(acc)
acc2 = Account(300)
acc + acc2
acc < acc2

# %%
# héritage
from datetime import datetime
class Client:
    def __init__(self, f: str, n: str, dj: str) -> None:
        self.firstname = f
        self.lastname = n
        self.date_joint = datetime.strptime(dj, "%Y-%m-%d")
    
    def get_full_name(self):
        return f"{self.firstname.capitalize()} {self.lastname.upper()}"
    
    def get_date_joint(self, _format: str):
        return self.date_joint.strftime(_format)

cl = Client("matt", "lamam", "2022-10-13")
cl.get_full_name()
cl.get_date_joint("%d/%m/%Y")
# %%
