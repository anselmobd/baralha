from pprint import pprint
from random import randint

from baralla.tipo_jogo import TipoJogo


class Jogador:

    def __init__(self, nome) -> None:
        self.nome = nome

        self._mao = []
        self.monte = []
        self.tipo_jogo = None
        self.caracteristicas = None

    def __str__(self) -> str:
        return self.nome

    def __repr__(self) -> str:
        return f"Jogador({self.nome})"

    def recebe_carta(self, carta):
        self._mao.append(carta)

    @property
    def mao(self):
        return self._mao

    @property
    def tem_carta(self):
        return len(self._mao) != 0

    def set_tipo_jogo(self, tipo_jogo):
        self.tipo_jogo = tipo_jogo
        self.caracteristicas = TipoJogo(tipo_jogo).definicao

    def joga(self, mesa):
        """Aqui entrará a lógica de decisão do jogador"""
        mesa.coloca_carta(self.mao.pop(), self)
