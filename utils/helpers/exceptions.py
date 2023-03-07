class ValuesError(Exception):
    def __init__(self, values) -> None:
        self.__values = values

    def __str__(self) -> str:
        return f"{','.join(self.__values)} non convertibles !!"   