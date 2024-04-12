# %%
import csv

# encodage windows
with open("./dns_100000.csv", mode="r", encoding="iso-8859-15") as f:
    csv_rd = csv.reader(
        f,
        delimiter=";",
        quotechar='"',
        quoting=csv.QUOTE_NONE
    )
    i = 0
    # dégager le header
    next(csv_rd)
    countries = {}
    for line in csv_rd:
        # if i == 0:
        #     i += 1
        #     continue
        if line[1] in countries:
            countries[line[1]] += 1
        else:
            countries[line[1]] = 1
        if i > 100:
            break
        # print(line)
        i += 1
    
# tri sur un dictionnaire
# conversion en dict  => instanciation d'un objet dict selon un objet de départ
dict(sorted(countries.items(), key=lambda t: t[1], reverse=True))

# %%

class MyIterator:

    def __init__(self, limit=10) -> None:
        self.__limit = limit


    def __iter__(self):
        self.__counter = 0
        return self
    
    def __next__(self):
        if self.__counter < self.__limit:
            val = self.__counter
            self.__counter += 1
            return val
        else:
            raise StopIteration

mit = MyIterator()
# iter appelle __iter__ => il recharge l'itérable avec un compteur
# itérateur
# iterator = iter(mit)
## next(): next appelle la méthode __next__ itération unique
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

for val in mit:
    print(val)
# %%
