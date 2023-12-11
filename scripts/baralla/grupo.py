from pprint import pprint
from random import randint

from baralla.jogador import Jogador


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

    def todos_jogam(self, mesa):
        for _ in self.jogadores:
            self.jogadores[self.idx_da_vez].joga(mesa)
            self.proximo()

    def str_estado(self):
        return {
            self.jogadores[jogador].nome: self.jogadores[jogador].mao
            for jogador in self.jogadores
        }
