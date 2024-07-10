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
# annotations importantes pour l'autocomplétion des variables locales !!!
def my_upper(_str: str):
  return _str.upper()

# %%
#  injection de dépendance

class Client:
  def __init__(self, firstname: str, name: str):
    self.__firstname = firstname
    self.__name = name
  
  def get_full_name(self): 
    return f"{self.__firstname.capitalize()} {self.__name.upper()}"
class BankAccount:
  def __init__(self, balance: float, owner: Client):
    self.__balance = balance
    self.__owner = owner
 

  def get_client_name(self): 
    # injection de dépendance
    # la classe BankAccount ne connâit que les signatures des méthodes publiques
    # délégation du nom complet du client à l'objet client
    return self.__owner.get_full_name() 

cl = Client("matt", "lamam")
# un compte a un client
acc = BankAccount(200, cl)

acc.get_client_name()
# %%
# héritage "simple"

class Person:
  def __init__(self, f, n):
    self.__f = f
    self.__n = n
  
  def get_full_name(self): 
    return f"{self.__f.capitalize()} {self.__n.upper()}"

class Client(Person):
  # surcharge de méthode = on hérite de la méthode parente 
  # et ajoute des comportements personnels
  def __init__(self, _id, f, n):
    self.__id = _id
    # super(): appel à l'initialiseur de la classe mère (Person)
    # fournit les attributs d'objet de l'objet courant (cl)
    super().__init__(f, n)

cl = Client(34534, "bob", "smith")
# méthode héritée
print(cl.get_full_name())
# print(cl._Person__f)
# %%

from datetime import datetime
 
class Person:
  """
  class
  """
  def __init__(self, f, n):
    self.__f = f
    self.__n = n
 
  def get_full_name(self):
    return f"{self.__f.capitalize()} {self.__n.upper()}"
 
class Client(Person):
  __format = "%Y-%m-%d"

  def __init__(self, _id, f, n, date_joint):
    self.__id = _id
    self.__date_joint = datetime.strptime(date_joint, self.__format)
    super().__init__(f, n)
 
  def get_date_joint (self) :
      return self.__date_joint.strftime(self.__format)
 
  def check_3month (self) :
      now = datetime.now()
      duree = now - self.__date_joint
      return duree.days > 90
 
cl = Client(34534, "bob", "smith", "1977-09-09")

print(cl.get_full_name())
print(cl.get_date_joint())
print(cl.check_3month())

# %%

# en python tout est objet !!!!
class Truc:
  pass
x = 1
t = Truc()

type(x), type(t)
isinstance(t, Truc), isinstance(x, int)

# conversion de 1 en "1"
# instanciation d'un objet "1" 
# à partir d'un paramètre 1 
# du __init__ de la classe str
_str = str(1)
# %%
