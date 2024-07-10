# from project.calc import ctrl_mean
# ATTENTION: ne fonctionne pas si l'on a pas l'import du __init__.py !!!
from project import ctrl_mean

if __name__ == "__main__":
    print(ctrl_mean("-1,1", debug=True))