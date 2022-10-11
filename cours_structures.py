# %%
x = 10

if x > 0: print("positif")
elif not x: print('nul')
else: print("négatif")

# %%
# opérateur ternaire
cond = True
if cond: param = "expected_value"
else: param = "default_value"

param = "expected_value" if cond else "default_value"

# %%
# types de boucles for
# 1. conserver la liste d'origine
fruits = ["pomme", "poire", "banane"]
fruits_maj = []
for fruit in fruits:
    fruits_maj.append(fruit.upper())
fruits_maj
# %%
# 2. sans conserver la liste d'origine
fruits = ["pomme", "poire", "banane"]
# on génère les indices de la liste et on utilise [] 
# pour accéder aux valeurs
for i in range(len(fruits)):
    fruits[i] = fruits[i].upper()
fruits

# %%
# 2 bis.
fruits = ["pomme", "poire", "banane"]
for i, fruit in enumerate(fruits):
    fruits[i] = fruit.upper()
fruits
# %%
# 3. listes en intension
fruits = ["pomme", "poire", "banane"]

# liste des fruit.upper() pour fruit pris dans fruits
[ fruit.upper() for fruit in fruits ]
# %%
# liste en intension avec filtre
fruits = ["pomme", "poire", "banane"]

[ fruit.upper() for fruit in fruits if fruit[0] == "p" ]
{ f: f.upper() for f in fruits if f[0] == "p" }
# %%

# boucle while
a, b = 0, 1

# while condition:
while b < 100:
    c = a + b
    a = b
    # le bloc du while doit modifier la condition
    # sinon boucle infinie
    b = c
    print(b)


# %%
# petit point sur l'affectation
a, b = 0, 1

while b < 100:
    # a = b
    # # ne marche pas car a a changé
    # b = a + b
    # marche car le a à droite vaut sa valeur de départ
    a, b = b, a + b
    print(b)
# %%

a, b = 0, 1

while True:
    a, b = b, a + b
    # interrompt l'itération courante
    # et passe à la suivante
    if not b % 2: continue
    print(b)
    # sortir immédiatement si cond
    if b > 100: break
# %%
# else après for ou while: voir exo moyenne

# %%
# instruciton pass: sert à structurer un code
# àvenir (bloc vide)
# ...programme...
cond = True

if cond:
    # TODO
    pass
# %%
