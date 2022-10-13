# %%
from utils.misc import strip_lil_words
from string import punctuation
import re


class Cleaner:
    
    def __init__(self, text: str, punc: str=punctuation, min_length: int=4) -> None:
        self.__text = text
        self.__punc = punc
        self.__min_length = min_length
    
    def __clean_punc(self):
        self.__text = re.sub(f"[{self.__punc}]", " ", self.__text)

    def __clean_crlf(self):
        # ? en regex: 0 ou 1 fois pour le caractère précédent
        self.__text = re.sub("\\r?\\n", " ", self.__text)

    def __clean_spaces(self):
        # + en regex: au moins 1 fois pour le caractère précédent
        self.__text = re.sub(" +", " ", self.__text)

    def __clean_little_words(self):
        self.__text = strip_lil_words(self.__text, self.__min_length)

    def clean(self):
        self.__clean_punc()
        self.__clean_crlf()
        self.__clean_spaces()
        self.__clean_little_words()
        return self.__text.lower()
