# %%
# manipulations sur les nombres
# 1. saisir trois fois trois entiers au clavier
# 2. calculer la moyenne arithmétique
# 3. calculer l'écart type
# std = sqrt(1/n sum((x - moy)**2))
# utiliser la fonction round()
# pour afficher les résultats avec 2 chiffres significatifs

n1 = input("entier 1: ")
n2 = input("entier 2: ")
n3 = input("entier 3: ")

n1 = int(n1)
n2 = int(n2)
n3 = int(n3)

moy = ( n1 + n2 + n3 ) / 3
std = (1/3 * ((n1 - moy)**2 + (n2 - moy)**2 + (n3 - moy)**2))**0.5
print("la moyenne de ", n1, n2, n3, ":", round(moy, 2))
print("l'écart type de ", n1, n2, n3, ":", round(std, 2))
# %%
