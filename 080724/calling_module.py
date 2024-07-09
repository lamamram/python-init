import imported_module



if __name__ == "__main__":
    # espace du nom du module: garantit l'unicité du nom
    print(imported_module.my_var)
    print(imported_module.my_func())

    # print(dir(imported_module))
    print(imported_module.__name__)

    print(__name__)
# ---------------------------------------
# import sans espace de nom
# from imported_module import my_func
# idem avec alias
# from imported_module import my_func as mine_my_func

# def my_func():
#     return "prout"

# print(mine_my_func())

# ---------------------------------------------
# import de tous les noms sans espace de noms
# from imported_module import *

# print(my_func())
# print(my_var)
