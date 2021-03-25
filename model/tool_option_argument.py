from db import connect


class ToolOptionArgument:

    __option: str
    __argument: str

    def __init__(self, option, argument):
        pass

    def option(self) -> str:
        return self.__option

    def argument(self) -> str:
        return self.__argument
