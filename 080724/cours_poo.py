# %%
# classe et instance

class BankAccount: 
  # attributs: variables internes
  _id = 0
  balance = 0.

# création de la variable acc de type BankAccount
# instanciation de l'objet "acc" de classe BankAccount
acc = BankAccount()
# manipulation des attributs hérités de la classe
acc._id = 21345345
print(acc._id)

acc2 = BankAccount()
acc2._id = 245665
print(acc2._id)
# %%
class BankAccount: 
  _id = 0
  balance = 0.
  
  # méthodes: fonctions internes
  def is_overdraft(self):
    return self.balance < 0

acc = BankAccount()
acc.balance = 100
print(acc.is_overdraft()) # acc est "self" donc pas de paramètre !!
# %%

class BankAccount: 
  # attribut privé (de classe)
  __id = 0
  # méthodes publiques
  def get_id(self):
    """format""" 
    return self.__id # lecture depuis la classe !!
  
  def set_id(self, _id):
    """checks""" 
    self.__id = _id # écriture depuis la classe !!

acc = BankAccount()
# encapsulation de l'attribut privé __id
# print(acc.__id) # AttributeError

acc.set_id(3434555) # setter: méthode publique pour écrire un attribut
acc.__id = 666 # BIZARRE
print(acc.get_id()) # getter: méthode publique pour lire un attribut

## pas un vrai langage de POO parce qu'on peut utiliser les attributs privé
# avec la nomenclature <object>._<class_name>__<attribute>
## DONC depuis l'extérieur a priori __id n'existe pas !!!
## mais on peut créer un attribut __id qui n'est pas le VRAI attribut privé
## et qui ne sera jamais utilisé dans la classe avec "self"
print(acc._BankAccount__id)
print(acc.__id)
# %%
from abc import ABC

# classe abstraite
## utilisation d'une classe abstraite qui donne l'interface standard 
# à utiliser pour les classes concrètes (métier)
class BankAccountAbstract(ABC):
    ## interface de la classe => présentation des méthodes
    def __init__(self, _id, balance): pass
    def __str__(self) -> str: pass
    def __add__(self, alt_acc): pass
    def get_id(self): pass
    def get_balance(self): pass

# méthodes magiques
class BankAccount(BankAccountAbstract):
  # génére et renseigne des attributs d'objet dès l'instanciation
  def __init__(self, _id: int, balance: float=100.):
    self.__id = _id
    self.__balance = balance

  def get_id(self):
    return self.__id
  
  def get_balance(self):
    return self.__balance

  # donne un sens à l'affichage et la conversion en str de l'objet
  def __str__(self) -> str: 
    return f"id: {self.__id} balance: {self.__balance}"

  def __add__(self, alt_acc: BankAccountAbstract):
    # çà fonctionne AUSSI avec alt_acc.__balance (censé être privé) !!!!
    return self.__balance + alt_acc.get_balance()

  def __getitem__(self, ind: int):
    return ind

acc = BankAccount(34554) # exécute automatiquement la méthode __init__
acc2 = BankAccount(3534, 200)
print(acc.get_id())
print(acc)
acc + acc2

acc[2]
# print(acc), str(acc) # exécute __str__
# %%

def my_upper(_str: str):
  return _str.upper()
