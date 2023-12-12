from pprint import pprint, pformat

from baralla.tipo_jogo import TipoJogo
from baralla.baralho import Baralho
from baralla.grupo import Grupo


class Mesa:

    def __init__(self) -> None:
        self.trunfo = None
        self.cartas = []

    def set_trunfo(self, carta):
        self.trunfo = carta

    def coloca_carta(self, carta, jogador):
        self.cartas.append({
            'carta': carta,
            'jogador': jogador,
        })

    def __str__(self) -> str:
        return pformat([
            carta['carta']
            for carta in self.cartas
        ])

    def __repr__(self) -> str:
        return pformat(self.cartas)
