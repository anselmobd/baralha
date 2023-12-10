from pprint import pprint
from random import randint

from baralla.tipo_baralho import TipoBaralho


class Carta:

    def __init__(self, numero, naipe) -> None:
        self.numero = numero
        self.naipe = naipe

    def __str__(self) -> str:
        return f"{self.numero}{self.naipe}"

    def __repr__(self) -> str:
        return repr(str(self))
