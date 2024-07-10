from string import punctuation
from text_analyser.cleaner import Cleaner

class OccurencesCounter:
    def __init__(self, text, punc=punctuation, min_words=3):
        self.__text = Cleaner(text, punc=punc, min_meaning_words=min_words).clean()
        self.__occurences = {}
    
    def get_occurences(self, max_occurences=5):
        # alimentation du compteur d'occurences
        for word in self.__text.split():
            if word in self.__occurences:
                self.__occurences[word] += 1
            else:
                self.__occurences[word] = 1
        # transformations: 
        # 1/ self.__occurences.items() : dico => list[tuple]
        # 2/ sorted : trier la liste de tuples selon l'occurence décroissante
        # 3/ [:5] => tronquer aux 5 premiers tuples de la liste de tuples triée
        # 4/ dict() : transformation list[tuple] => dico
        self.__occurences = dict(sorted(self.__occurences.items(), key=lambda tup: tup[1], reverse=True)[:max_occurences])
        return self.__occurences

