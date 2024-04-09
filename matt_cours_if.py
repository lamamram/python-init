# %%
x = input("tapez un entier: ")
print(type(x))
x = int(x)
# unpacking en python
print(x < 5, x == 10, x != 33, x >= 8)
equal_to_10 = x == 10 
# on teste une valeur booléene
if equal_to_10:
    # on teste une expression entière
    # if (x + 2) % 4 => 0 : False, tout le reste True
    if (x + 2) % 4 == 0:
        print("10 +  2 est divisible par 4 !!") 
    print("x est 10 !!")
elif x != 33:
    print("pas 33")
else:
    print("x n'est pas 10 mais c'est 33 !!")
# if not None:
#     print("pas Rien c'est qqch !!")
# opérateur is et opérateur logique not
if x is not None:
    print(x)

# %%
string = ""
if not "":
    print("chaine vide")
# %%
# l'opérateur ternaire
value = None
condition = True
if condition:
    value = "truc"
else:
    value = "something"

# la valeur est "truc" si la condition est vraie, sinon c'est "something"
value = "truc" if condition else "something"
value
# %%