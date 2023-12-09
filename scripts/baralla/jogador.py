from pprint import pprint
from random import randint


class Jogador:

    def __init__(self, nome) -> None:
        self.nome = nome

    def __str__(self) -> str:
        return self.nome


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

    def adiciona(self, jogador):
        self.jogadores[self.num_jogadores] = jogador

    def sorteia(self):
        self._idx_da_vez = randint(0, self.num_jogadores - 1)

    def proximo(self):
        self._idx_da_vez = (self._idx_da_vez + 1) % self.num_jogadores
