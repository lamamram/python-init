from string import punctuation
# Regular Expression
import re

class Cleaner:
    def __init__(self, text: str, punc: str=punctuation, min_meaning_words=3):
        self.__punc = punc
        self.__text = text
        self.__min_meaning_words = min_meaning_words

    def __clean_punc(self):
        # autant d 'iteration du texte qu'il ya de caractère
        # for char in punctuation:
        #     self._text = self.__text.replace(char, " ")
        # lire 1 fois le texte et à chaque substitue les carachtre
        self.__text = re.sub(f"[{self.__punc}]", " ", self.__text)

    # CRLF Carriage Return (\r) Line Feed (\n) windows => \r\n, unix => \n
    # (a|b) : alternative: a ou b
    # x? : x 0 fois ou 1 fois 
    # x* : n'importe quelle fois
    # x+ : 1 fois ou plusieurs
    # x{2}: 2 fois
    def __clean_crlf(self):
        self.__text = re.sub(f"\\r?\\n", " ", self.__text)

    def __clean_spaces(self):
        self.__text = re.sub(f" +", " ", self.__text)
    
    def __clean_little_words(self):
        self.__text = " ".join(list(filter(lambda word: len(word) > 3, self.__text.split()))) 
    
    def clean(self):
        self.__clean_punc()
        self.__clean_crlf()
        self.__clean_spaces()
        self.__clean_little_words()
        return self.__text.lower()