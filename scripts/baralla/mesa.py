from pprint import pprint, pformat

from baralla.tipo_jogo import TipoJogo
from baralla.baralho import Baralho
from baralla.grupo import Grupo


class Mesa:

    def __init__(self) -> None:
        self.trumfo = None
        self.baralho = None
        self.cartas = []

    def set_trumfo(self, carta):
        self.trumfo = carta

    def set_baralho(self, baralho):
        self.baralho = baralho

    def coloca_carta(self, carta, jogador):
        self.cartas.append({
            'carta': carta,
            'jogador': jogador,
        })

    # debug output

    def __repr__(self) -> str:
        return pformat({
            'trumfo': self.trumfo,
            'baralho': self.baralho,
            'cartas': self.cartas,
        })
