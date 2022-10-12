# %%
# CamelCase: les mots sont séparés par des majuscules
class Account:
    # attribut de classe
    balance = 100.

    # méthode
    # le premier paramètre de toute méthode de classe (hors static)
    # représente une instance de la classe, et est nommé par convention self
    def deposit(self, amount: float):
        # on accède aux attributs à travers self 
        self.balance += amount

acc = Account()
acc.balance
# quand on appelle une méthode, on ne tient pas compte
# du premier paramètre self de la def, car acc est self
acc.deposit(200)
acc.balance
# %%
