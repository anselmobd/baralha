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

    def recebe_carta(self, carta):
        self._mao.append(carta)

    @property
    def mao(self):
        return self._mao

    def set_tipo_jogo(self, tipo_jogo):
        self.tipo_jogo = tipo_jogo
        self.caracteristicas = TipoJogo(tipo_jogo).caracteristicas


class Grupo:

    def __init__(self) -> None:
        self.jogadores = {}
        self._idx_da_vez = 0

    @property
    def num_jogadores(self):
        return len(self.jogadores)

    @property
    def da_vez(self):
        return self.jogadores.get(self._idx_da_vez, "")

    @property
    def idx_da_vez(self):
        return self._idx_da_vez

    @property
    def get_jogador(self) -> Jogador:
        return self.jogadores[self.idx_da_vez]

    def adiciona(self, jogador):
        self.jogadores[self.num_jogadores] = jogador

    def sorteia(self):
        self._idx_da_vez = randint(0, self.num_jogadores - 1)

    def proximo(self):
        self._idx_da_vez = (self._idx_da_vez + 1) % self.num_jogadores

    def set_tipo_jogo(self, tipo_jogo):
        for idx_jogador in self.jogadores:
            self.jogadores[idx_jogador].set_tipo_jogo = tipo_jogo
